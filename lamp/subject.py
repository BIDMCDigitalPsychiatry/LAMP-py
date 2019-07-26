import pandas as pd 
import numpy as np
import datetime
import os
import math
import lamp
import itertools
from functools import reduce
#import

class Subject():
	"""
	Create subject dataframe
	
	"""
	def __init__(self, id, domains=None, age=None, race=None, sex=None, beiwe_id=None, beiwe_filepath=None):
		self.id = id
		self.domains = domains
		self.beiwe_id = beiwe_id
		self.beiwe_filepath = beiwe_filepath
		self.df = self.create_subject_df()
		
		self.age = age
		self.race = race
		self.sex = sex
		
		self.impute_status = False
		self.bin_status = False
		self.normalize_status = False
		
	
	@property
	def id(self):
		return self._id
	
	@property
	def age(self):
		return self._age
	
	@property
	def race(self):
		return self._race
	
	@property
	def sex(self):
		return self._sex
	
	@property
	def beiwe_id(self):
		return self._beiwe_id
	
	@property
	def beiwe_filepath(self):
		return self._beiwe_filepath
	
	@id.setter
	def id(self, value):
		self._id = value
		
	@age.setter
	def age(self, value):
		self._age = value
	
	@race.setter
	def race(self, value):
		self._race = value
		
	@sex.setter
	def sex(self, value):
		self._sex = value
		
	@beiwe_id.setter
	def beiwe_id(self, value):
		self._beiwe_id = value
		
	@beiwe_filepath.setter
	def beiwe_filepath(self, value):
		self._beiwe_filepath = value
	
	def reset(self):
		"""
		Resets the subject's df to be the original version
		"""
		self.df = self.create_subject_df()
		self.impute_status, self.bin_status, self.normalize_status = False, False, False
		
	def domain_check(self, domains):
		"""
		If domains is passed in, just return it.
		
		Else, see if domains is set as object attribute
		"""
		if domains is None:
			if not hasattr(self, 'domains'):
				raise AttributeError('Domains were not set for cohort and were not provided.')
			domains = self.domains
		return domains
		
	
	def survey_results(self, participant=None, datetime_object=False):
		"""
		Get survey events for participant
		
		:param participant (str): the LAMP ID for participant. If not provided, then take subjects
		:param datetime_object (bool): flag that determines whether survey timestamps are given in Unix timestamp or datetime objects
		"""
		def survey_event_parse(survey):
			"""
			Helper function that parses survey event 

			Parameters:
			survey (list): contains all questions in particicular survey 

			Returns:
				survey_result (dict): maps relevant question categories to a score
			"""
			survey_result = {}
			for event in survey:
				question = event['item']

				#Check if question in one of the categories
				if question in lamp.SurveyQuestionDict:
					category = lamp.SurveyQuestionDict[question]

					#If reverse coded social question, then flip the score
					if category == "Social_Reverse":
						category = 'Social'
						score = 3 - event['value']
					elif category == 'Medication':
						score = 3 - event['value']
					else:
						score = event['value']

					if category in survey_result: survey_result[category].append(score) 
					else: survey_result[category] = [score]

			#Take mean for each cat
			for cat in survey_result:
				survey_result[cat] = float(sum(survey_result[cat])/len(survey_result[cat]))
			return survey_result 

		participant_surveys = {} #initialize dict mapping survey_type to occurence of scores
		if participant is None:
			participant = self.id
		participant_results = lamp.result_event.result_event_all_by_participant(participant).data
		for res in participant_results:
			#Check if its a survey event
			if 'survey_name' in res['static_data'].keys():
				try:
					survey_result = survey_event_parse(res['temporal_events'])
				except Exception as e:
					print(e)
					continue

				survey_time = res['timestamp']
				if datetime_object:
					survey_time = datetime.datetime.utcfromtimestamp(survey_time/1000).date()
				#Add to master dictionary
				for category in survey_result:
					if category not in participant_surveys:
						participant_surveys[category] = [(survey_result[category], survey_time)]
					else:
						participant_surveys[category].append((survey_result[category], survey_time))

		return participant_surveys
	
	def create_subject_df(self, ndays=120):
	
	
		subject_surveys = self.survey_results()
		
		#Find the first, last date
		try:
			first_day = datetime.datetime.utcfromtimestamp(sorted([subject_surveys[key][0][1]/1000 for key in subject_surveys])[0]).date()
			last_day = datetime.datetime.utcfromtimestamp(sorted([subject_surveys[key][-1][1]/1000 for key in subject_surveys])[-1]).date()
			number_of_days = (last_day - first_day).days
		except Exception as e:
			print(e)
		
		#Create dateframe for the number of days that have data; cap at 'ndays' if this number is large
		df = pd.DataFrame({'Date': [first_day + datetime.timedelta(days=x) for x in range(min(number_of_days, ndays))], 'id':self.id})

		#Create null dataframes for all survey types
		for cat in #['Mood', 'Anxiety', 'Psychosis', 'Sleep', 'Social']:
			df[cat] = np.nan
			
		#Parse surveys
		for cat in subject_surveys:
			df[cat] = np.nan
			for event in subject_surveys[cat]:
				event_day = datetime.datetime.utcfromtimestamp(event[1]/1000).date()
				df.loc[df['Date'] == event_day, cat] = event[0]

		#Convert to Date to string
		df['Date'] = df['Date'].astype(str)

		#Take into account medication
		if 'Medication' not in list(df):
			df['Medication'] = [np.nan]*df.index.size


		#Try beta vals
		beta_val_list = pd.read_csv('/home/ec2-user/Data/LAMP Part 1/daily_beta_vals.csv')
		subj_beta_vals = beta_val_list.loc[beta_val_list['id'] == self.id]
		if subj_beta_vals.empty:
			df['beta_a'] = np.nan
			df['beta_b'] = np.nan
		else:
			
			df = pd.merge(df, subj_beta_vals[['Date', 'beta_a', 'beta_b']], on='Date', how='outer')
		
		#print(df)
		def parse_beiwe_pipeline(subject_id, ndays=90):
			#Find beiwe id
			if self.beiwe_filepath is None:
				print('Beiwe filepath is not set. Please set filepath to add passive data to dataframe.')
				return None, None
			
			if not isinstance(self.beiwe_id, str):
				print('No beiwe file', subject_id)
				return None, None

			#Get step data
			try:
				steps_file = pd.read_csv(os.path.join(self.beiwe_filepath, self.beiwe_id, 'steps.csv'))
				steps_file['Date'] = steps_file['Date'].astype(str)

			except Exception as e:
				print(e)
				steps_file = None

			#Get sleep_data
			try:
				sleep_file = pd.read_csv(os.path.join(self.beiwe_filepath, self.beiwe_id, 'sleep_estimates.csv'))
				sleep_file['Date'] = sleep_file['Date'].astype(str)
			except:
				#print('No sleep file!')
				sleep_file = None

			return steps_file, sleep_file

		steps_file, sleep_file = parse_beiwe_pipeline(self.id)
		
		dataframes = [df]
		#print(dataframes)
		if steps_file is not None:
			dataframes.append(steps_file)

		if sleep_file is not None:
			dataframes.append(sleep_file)

		if steps_file is not None and sleep_file is not None:
			df_final = reduce(lambda left,right: pd.merge(left, right, on='Date', how='left'), dataframes)
		else:
			df_final = df
			
		return df_final
	
	def impute(self, domains):
		"""
		Get value for each column for each window
		"""
		if self.impute_status:
			print('Dataframe already imputed.')
			return

		weighted_dict = [0.05, 0.20, 0.40, 1.5, 0.4, 0.20, 0.05]

		#Get indices of all middle bin values; add them to new df
		for dom in domains:
			if dom not in self.df:
				continue
				
			dom_values = []

			for ind in range(len(self.df.index)):

				#Get indices
				middle_weight_index = 3
				starting_index = max(ind -3, 0)
				ending_index = min(ind + 4, 90)

				#Get slice values
				subj_slice = self.df.iloc[starting_index:ending_index]

				#Remove na
				subj_slice_no_nan = subj_slice[dom].dropna()
				slice_indices = subj_slice_no_nan.index

				if len(slice_indices) == 0:
					dom_values.append(np.nan)
					continue

				#Match slice index with weight index
				weighted_dict_vals = [weighted_dict[middle_weight_index - (ind - slice_i)] for slice_i in slice_indices]

				#Find total in bin
				slice_val = sum(subj_slice_no_nan * [val / sum(weighted_dict_vals) for val in weighted_dict_vals])
				dom_values.append(slice_val)
			
			self.df[dom] = dom_values
		
		self.impute_status = True

	
	def bin(self, domains, window_size=3, shift=None):
		"""
		Bin dataframe
		
		:param domains (list): the domains to bin 
		:window_size (int): the size of the bins (in days)
		:shift (int): the day of the week to start the binning on (Monday == 0)
		
		"""
		
		domains = self.domain_check(domains)
		#Shift until Monday
		df_copy = self.df.copy()
		if shift not is None:			
			dow = datetime.datetime.strptime(df_copy['Date'].values[0], '%Y-%m-%d').weekday()
			if dow > 0 and len(df_copy) > dow:
				df_copy = df_copy.shift(shift - dow)
				
		df_copy['bin'] = np.floor(df_copy.index / window_size )
		bins = df_copy.groupby('bin')
		subj_bin_df = pd.DataFrame(columns=['Bin Start Date', 'Bin End Date']+domains)
		for b in bins:
			bin_values = []
			#Add bin start/end dates
			start_date, end_date = b[1].iloc[0]['Date'], b[1].iloc[-1]['Date']
			bin_values.extend((start_date, end_date))
			for dom in domains:
				if dom in b[1].columns:
					bin_dom_value = b[1][dom].mean()
					bin_values.append(bin_dom_value)
				else:
					bin_values.append(np.nan)

			#Add date range
			subj_bin_df.loc[b[0]] = bin_values    

		subj_bin_df['id'] = self.id
		self.bins = subj_bin_df

	
	def normalize(self, domains, domain_means={}, domain_vars={}):
		"""
		Normalize columns values to 0 mean/ unit variance
		:param domain_means (dict): the mean for each column value
		:param domain_vars (dict): the variance for each column value
		
		If mean/var not provided, resort to in-sample normalization
		"""
		if self.normalize_status:
			print("Dataframe has already been normalized. Please reset dataframe if you wish to normalize it in a different way.")
			return
		
		domains = self.domain_check(domains)
		if domain_means == {} and domain_vars == {}:
			for dom in domains:
				if dom in self.df:
					domain_means[dom] = self.df[dom].mean()
					domain_vars[dom] = self.df[dom].std()
		
		for dom in domains:
			if dom in self.df.columns and dom in domain_means and dom in domain_vars:
				self.df[dom] = (self.df[dom] - domain_means[dom]) / domain_vars[dom]
		
		self.normalize_status = True
		
	def create_transition_dict(self, level):
		"""
		Create nested dictionary structure 
		
		:param level (int): the level dictionary structure. Must be >= 0
		"""
		trans_dict = {}
		for comb in itertools.product(('out', 'in'), repeat=level):
			trans_dict[comb] = {comb2:0 for comb2 in itertools.product(('out', 'in'), repeat=level)}
		return trans_dict
	
	
	def assign_transition_dict(self, trans_dict, row, row2):
		"""
		Increment transition dict
		"""
		label1 = tuple(['in' if col < 1.0 else 'out' for col in row])
		label2 = tuple(['in' if col < 1.0 else 'out' for col in row2])
		trans_dict[label1][label2] += 1
		
	def get_transitions(self, domains=None, joint_size=1):
		"""
		Count transition events for each col in subj_df
		"""
		domains = self.domain_check(domains)
		all_trans_dict = {}
		for dom_group in itertools.combinations(domains, r=joint_size):
			
			#Create trans dictionary
			group_dict = self.create_transition_dict(level=joint_size)
			
			#Find bins with values for each group
			good_bins = self.bins[list(dom_group)].dropna()

			#Assign
			row_iterator = good_bins.iterrows()
			try:
				last_i, last = next(row_iterator)
			except StopIteration:
				continue
			for index, row in row_iterator:
				if int(index) - int(last_i) <= 3:
					self.assign_transition_dict(group_dict, last, row)
				last_i, last = index, row
			
			all_trans_dict[dom_group] = group_dict
			
		return all_trans_dict
	
	def domain_bouts(self, domains=None):
		"""
		"""
		def parse_bout_list(bout_list, state, low_bouts, high_bouts):
			"""
			Helper function to parse bout list at end of bout
			"""
			if len(bout_list) == 1: bout_list.append(bout_list[-1] + 3) #edge case where last domain event is only one in its bout
				
			if state: low_bouts.append(float(bout_list[-1]) - float(bout_list[0]))
			else: high_bouts.append(float(bout_list[-1]) - float(bout_list[0]))
			return low_bouts, high_bouts
			
		domains = self.domain_check(domains)
		bout_dict = {}
		for dom in domains:
			if dom not in self.df:
				continue

			bout_list = [] #temporary list that contains times of current bout
			subj_dom = self.df.loc[self.df[dom].notnull(), dom]
			row_iterator = subj_dom.iteritems()
			try:
				last_day, last_val = next(row_iterator)
				bout_list.append(last_day)
				if last_val < 1.0: last_state = True #set this back on first val
				else: last_state = False
			except StopIteration:
				continue
				
			bout_dict[dom] = {}
			low_bouts, high_bouts = [], [] #duration of all in-range bouts
			low_bouts_end, high_bouts_end = 0, 0 #counter the keep track of # of ended bout things
			for day, val in row_iterator:
				if val < 1.0: state = True
				else: state = False
					
				if last_state == state and day - last_day <= 6: #continue bout
					bout_list.append(day)
					
				else: #discontinue bout
					if day - last_day > 8: 
						bout_list.append(last_day + 3) #If adjacent rows are day outside threshold, discontinue bout;cap last bout at 3 days past last activity	
						if last_state: low_bouts_end += 1
						else: high_bouts_end += 1
					else: bout_list.append(day) #then normal switch
		
					low_bouts, high_bouts = parse_bout_list(bout_list, last_state, low_bouts, high_bouts)
					bout_list = [day]

				last_day, last_val = day, val
				last_state = state
			
			low_bouts, high_bouts = parse_bout_list(bout_list, last_state, low_bouts, high_bouts) #parse last bout
			bout_dict[dom]['low'], bout_dict[dom]['high'] = [float(b) for b in low_bouts], [float(b) for b in high_bouts]
			bout_dict[dom]['low ends'], bout_dict[dom]['high ends'] = low_bouts_end, high_bouts_end

		return bout_dict

