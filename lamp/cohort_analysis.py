import statistics
from survey_question_dict import SurveyQuestionDict
import datetime
from functools import reduce
import pandas as pd
import numpy as np
import lamp
import lifelines
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt



def do_cohort_analysis(cohorts):
	"""
	Perform fragmentation analsis given list of cohorts
	"""

	#print([c for c in cohorts[0]['id']])

	parsed_cohorts = [pd.concat([subject_dataframe(subj) for subj in [c for c in cohort['id']]], sort=True) for cohort in cohorts]
	
	cohorts_means = get_mean_statistics(parsed_cohorts)
	print('Cohorts Means', cohorts_means)
	cohorts_usage = usage_plot(parsed_cohorts)
	print('Cohorts Usage', cohorts_usage)
	cohorts_binarized = [binarize_cohort(cohort) for cohort in parsed_cohorts]
	#cohorts_mssd = [get_mssd(norm) for norm in cohorts_binarized]
	cohorts_frag = [fragmentation(norm) for norm in cohorts_binarized]
	return cohorts_frag, parsed_cohorts    
	
	
def get_mssd(old_norm):
	
	norm_column = ['Anxiety', 'Psychosis', 'Mood', 'Medication', 'Social', 'Sleep']
	old_mssd_df = pd.DataFrame(columns=norm_column)
	row_list = []
	for subj_df in old_norm:

		row = []
		for col in norm_column:
			#Filter out Nan
			filtered_df = subj_df[subj_df[col].notnull()]
			mssd_col = ((filtered_df[col] - filtered_df[col].shift(1))**2)
			mssd = mssd_col.sum() / (mssd_col.size - 1)
			#print(mssd)
			row.append(mssd)
		row.append(subj_df['id'].iloc[0])
		row_list.append(row)

	old_mssd_df = pd.DataFrame(row_list, columns=norm_column+['id'])
	
	return old_mssd_df



#Fragmentation 

def fragmentation(old_norm):

	norm_column = ['Anxiety', 'Psychosis', 'Mood', 'Medication', 'Social', 'Sleep']
	lambda_dict = {}
	for subj_df in old_norm:
		subj = subj_df['id'].iloc[0]
		#print(subj)
		for col in norm_column:
			mask_col = col + ' Mask'
			if mask_col not in lambda_dict:
				lambda_dict[mask_col] = {'in':[], 'out':[]}

			filtered_mask_col = subj_df[subj_df[mask_col].notnull()][mask_col]

			in_range = True
			in_bouts = [] #duration of all in-range bouts
			out_bouts = []
			bout_list = [] #temporary list that contains times of current bout
			fragmentation_dict = [0, 0]

			for time in filtered_mask_col.index:

				val = filtered_mask_col.loc[time]

				try:
					if val == 0.0:
						temp = True
						fragmentation_dict[0] += 1
					else:
						temp = False
						fragmentation_dict[1] += 1
				except:
					print('BAD!', mask_col)
					break

				if in_range != temp: #then we switched states

					if len(bout_list) == 0: #edge case where bout list is empty due to first data point not being in range
						time_val = time
					elif len(bout_list) == 1: #edge case where bout duration is 1
						time_val = time - bout_list[0]#set it to interval between switch
					else:
						time_val = float(bout_list[-1]) - float(bout_list[0])

					if in_range == True: #place time val in in_bout
						in_bouts.append(time_val)
					else:
						out_bouts.append(time_val)

					bout_list = [time]
					in_range = temp

				else:
					bout_list.append(time)

			#Take care of case where end of list is not transition
			if len(bout_list) > 0:
				if len(bout_list) == 1: #edge case where bout duration is 1
					time_val = bout_list[0] - filtered_mask_col.index[-2] #set it to interval between transition
				else:
					time_val = float(bout_list[-1]) - float(bout_list[0])
				if in_range == True: #place time val in in_bout
					in_bouts.append(time_val)
				else:
					out_bouts.append(time_val)

			in_bouts = [float(b) for b in in_bouts]
			out_bouts = [float(b) for b in out_bouts]

	#         print(filtered_mask_col)
	#         print(in_bouts, out_bouts)
			#Calculate in lambda
			if len(in_bouts) > 0:
				try:
					in_lambda = 1.0/float(statistics.mean(in_bouts))
					lambda_dict[mask_col]['in'].append((in_lambda, subj))
				except:
					pass
				#print("In Lambda", in_lambda)

			if len(out_bouts) > 0:
				try:
					out_lambda = 1.0/float(statistics.mean(out_bouts))
					lambda_dict[mask_col]['out'].append((out_lambda, subj))
				except:
					pass
				#print("Out Lambda", out_lambda)
	return lambda_dict

def lambda_dict_avg(lam_dict, cat='Medication Mask'):

	lam_df = pd.DataFrame()
	#print(statistics.mean([x[0] for x in lam_dict[cat][0]]))
	#for cat in lam_dict:
	try:
		lam_df[cat] = [statistics.mean([x[0] for x in lam_dict[cat][0]]), statistics.stdev([x[0] for x in lam_dict[cat][0]]),
					   statistics.mean([x[0] for x in lam_dict[cat][1]]), statistics.stdev([x[0] for x in lam_dict[cat][1]])] 
	except Exception as e:
		pass
	print(lam_df)
	lam_df = lam_df.transpose()
	lam_df.columns = ['Lambda_In', 'Lambda_In_Std','Lambda_Out', 'Lambda_Out_Stdev']
	return lam_df

def binarize_cohort(cohort, sample_normalization=True, norm_columns=['Anxiety', 'Psychosis', 'Mood', 'Medication', 'Social', 'Sleep', 'Sleep Duration', 'Steps', 'beta_a', 'beta_b']):
	"""
	Normalize the data in dataframe and create mask for in/out of range
	
	:param cohort (df): dataframe containing active and passive data for participants in cohort
	:param sample_normalization (bool): indicates whether or not sample or population normalization is performed
	
	:return old_norm (df): 
	"""
	def col_normalization(subj_df, cols):
		
		for col in cols:
			if subj_df[col].std() == 0.0: #then just center values around 0
				subj_df.loc[subj_df[col].notnull(), col] = 0.0
			else:
				subj_df.loc[:,col] = (subj_df[col] - subj_df[col].mean()) / subj_df[col].std()
			subj_df[col+' Mask'] = [1 if x >= 1.0 else 0 if x < 1.0 else np.nan for x in subj_df[col]]
			
		return subj_df
			
	if sample_normalization:
		old_norm = []
		for subj, subj_df in cohort.groupby(cohort['id']):
			old_norm.append(col_normalization(subj_df, norm_columns))
		old_norm = pd.concat(old_norm).groupby('id')
							
	else:
		norm = col_normalization(cohort, norm_columns)
		#print(old_norm)
		old_norm = norm.groupby(norm['id'])
		
								  
	return old_norm


def usage_plot(cohorts):
	"""
	Plot usage participants in cohort
	
	
	"""
	kmf = lifelines.KaplanMeierFitter()
	norm_column = ['Anxiety', 'Mood', 'Psychosis', 'Sleep', 'Social', 'Medication']
	for cohort in cohorts:
		time_vals = []
		est_vals = []
		for day_group in cohort.groupby(cohort.index):
			#print(day_group[1][norm_column])
			for col in norm_column:
				time_vals += day_group[1][day_group[1][col].notnull()][col].index.tolist()
				est_vals += len(day_group[1][day_group[1][col].notnull()][col].index) * [1]

		kmf.fit(time_vals, est_vals)
		if 'ax' not in locals(): 
			ax = kmf.plot() 
		else: ax = kmf.plot(ax=ax)

	plt.xlabel('Day')
	plt.ylabel('Percentage of surveys remaining')
	#plt.show()
	plt.savefig('test_kmf.png')
	

def get_mean_statistics(cohorts, stats_test=False):
	"""
	Calculate mean and std deviation for each column in cohort
	"""
	norm_column = ['Anxiety', 'Mood', 'Psychosis', 'Sleep', 'Social', 'Medication']
	cohort_list = []
	for cohort in cohorts:
		val_map = {}
		for col in norm_column:
			try:
				val_map[col+' Mean'] = cohort[cohort[col].notnull()][col].mean()
				val_map[col+' StdDev'] = cohort[cohort[col].notnull()][col].std()
			except:
				pass
		cohort_list.append(val_map)
		
	if stats_test:
		high, low = cohorts[0], cohorts[1]
		for col in norm_column:
			print(col)
			print(cohort_list[0][col + ' Mean']) 
			print(cohort_list[1][col + ' Mean']) 
			print(ttest_ind(high[high[col].notnull()][col], low[low[col].notnull()][col]))

	return pd.DataFrame(cohort_list)
				
		
		
def get_survey_results(participant):
	"""
	Get survey events for participant
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
			if question in SurveyQuestionDict:
				category = SurveyQuestionDict[question]
				
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
			survey_result[cat] = float(sum(survey_result[cat])/len(survey_result[cat]))*(10.0/3.0)
		return survey_result 

	participant_surveys = {} #initialize dict mapping survey_type to occurence of scores
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
			#Add to master dictionary
			for category in survey_result:
				if category not in participant_surveys:
					participant_surveys[category] = [(survey_result[category], survey_time)]
				else:
					participant_surveys[category].append((survey_result[category], survey_time))
						  
	return participant_surveys


def subject_dataframe(subject_id, beiwe_filepath='/home/ec2-user/Data/Beiwe/Processed/current_pipeline_output/Processed_Data/Individual/', ndays=90):
	
	subject_surveys = lamp.cohort_analysis.get_survey_results(subject_id)

	#Find the first date
	try:
		first_day = datetime.datetime.utcfromtimestamp(sorted([subject_surveys[key][0][1]/1000 for key in subject_surveys])[0]).date()
	except:
		print(subject_id, subject_surveys)
		#return pd_DataFrame({'Date':[], 'id

	#Create dateframe, 90 days is standard
	df = pd.DataFrame({'Date': [first_day + datetime.timedelta(days=x) for x in range(ndays)], 'id':subject_id})

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
	subj_beta_vals = beta_val_list.loc[beta_val_list['id'] == subject_id]
	if subj_beta_vals.empty:
		df['beta_a'] = np.nan
		df['beta_b'] = np.nan
	else:
		df = pd.merge(df, subj_beta_vals[['Date', 'beta_a', 'beta_b']], on='Date')
		
	def parse_beiwe_pipeline(subject_id, beiwe_filepath, ndays=90):
		#Find beiwe id
		participant_data = pd.read_csv('/home/ec2-user/Data/LAMP Part 1/master_id_map.csv')
		beiwe_id = participant_data.loc[participant_data['id'] == subject_id, 'beiwe_id'].values[0]
		
		if beiwe_id == None:
			print('No beiwe file', subject_id)
			return None, None
			
		
		
		#Get step data
		
		try:
			
			steps_file = pd.read_csv(beiwe_filepath+beiwe_id+'/steps.csv')
			steps_file['Date'] = steps_file['Date'].astype(str)
		
		except Exception as e:
			print(e)
			steps_file = None
			
		#Get sleep_data
		try:
			sleep_file = pd.read_csv(beiwe_filepath+beiwe_id+'/sleep_estimates.csv')
			sleep_file['Date'] = sleep_file['Date'].astype(str)
		except:
			#print('No sleep file!')
			sleep_file = None
		
		return steps_file, sleep_file
					
	steps_file, sleep_file = parse_beiwe_pipeline(subject_id, beiwe_filepath=beiwe_filepath)
	
	dataframes = [df]
	#print(dataframes)
	if steps_file is not None:
		dataframes.append(steps_file)
		
	if sleep_file is not None:
		dataframes.append(sleep_file)
	
	if steps_file is not None and sleep_file is not None:
		
		df_final = reduce(lambda left,right: pd.merge(left, right, on='Date', how='left'), dataframes)
		return df_final
	
	return df





	

