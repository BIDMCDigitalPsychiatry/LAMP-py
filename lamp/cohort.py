import lamp
import numpy as np
from lamp import cohort_analysis
from functools import reduce
#from collections import Counter
"""
"""

class Cohort():
	"""
	"""
	def __init__(self, subjects, beiwe_filepath=None, ages=None, races=None, sexes=None, beiwe_ids=None):
		self.beiwe_filepath = beiwe_filepath
		self.ages = ages
		self.races = races
		self.sexes = sexes
		self.beiwe_ids = beiwe_ids
		self.init_subjects(subjects)
		
	def __iter__(self):
		for subj in self.subjects:
			yield subj
			
	def __len__(self):
		return len(self.subjects)
	
	def __getitem__(self, key):
		return self.subjects[key]
	
	@property
	def subjects(self):
		return self._subjects
	@property
	def beiwe_filepath(self):
		return self._beiwe_filepath
	
	@property
	def ages(self):
		return self._ages
	
	@property
	def races(self):
		return self._races

	@property
	def sexes(self):
		return self._sexes
	
	@property
	def beiwe_ids(self):
		return self._beiwe_ids
	
	@subjects.setter
	def subjects(self, value):
		self._subjects = value
		
	@beiwe_filepath.setter
	def beiwe_filepath(self, value):
		self._beiwe_filepath = value
	
	@ages.setter
	def ages(self, value):
		self._ages = value
		
	@races.setter	
	def races(self, value):
		self._races = value
		
	@sexes.setter	
	def sexes(self, value):
		self._sexes = value
		
	@beiwe_ids.setter
	def beiwe_ids(self, value):
		self._beiwe_ids = value
		
	def init_subjects(self, subjects):
		"""
		Initialize subjects in cohorts. Can take either Subject objects or subject ids
		"""
		self.subjects = []
		for subj in subjects:
			if isinstance(subj, lamp.Subject):
				self.subjects.append(subj)
				
			else:
				try:
					self.add_subject(subj)
				except Exception as e:
					print(e)
			
	def get_subject(self, subj_id):
		"""
		Get Subject object by id.
		
		If it doesn't exist, will return None
		"""
		for subj in self.subjects:
			if subj.id == subj_id:
				return subj
		
		print('Subject not found!')
		return None
	
	def add_subject(self, subject):
		subject_age = self.ages[subject] if self.ages and subject in self.ages else None
		
		subject_race = self.races[subject] if self.races and subject in self.races else None
		subject_sex = self.sexes[subject] if self.sexes and subject in self.sexes else None
		subject_beiwe_id = self.beiwe_ids[subject] if self.beiwe_ids and subject in self.beiwe_ids else None
		self.subjects.append(lamp.Subject(id = subject, beiwe_filepath = self.beiwe_filepath, age=subject_age, race=subject_race, sex=subject_sex, beiwe_id=subject_beiwe_id))
	
	
	def mean_age(self):
		"""
		Return mean, std age of subjects in cohort
		"""
		subject_ages = [subj.age for subj in self.subjects if subj.age is not None]
		if len(subject_ages) == 0:
			return None
		
		return np.mean(subject_ages)

	
	def std_age(self):
		"""
		Return std age of subjects in cohort
		"""
		subject_ages = [subj.age for subj in self.subjects if subj.age is not None]
		if len(subject_ages) == 0:
			return None
		
		return np.std(subject_ages)
		
	def set_ages(self, subject_ages):
		"""
		Set age for existing subject in cohort.
		
		If subject in dictionary cannot be found, id will be ignored
		
		:param subject_ages (dict): maps subject id to age
		"""
		
		for subj in self.subjects:
			if subj.id in subject_ages:
				subj.age = subject_ages[subj.id]
				
				
	def set_races(self, subject_races):
		"""
		Set race for existing subject in cohort.
		
		If subject in dictionary cannot be found, id will be ignored
		
		:param subject_races (dict): maps subject id to race
		"""
		
		for subj in self.subjects:
			if subj.id in subject_races:
				subj.race = subject_races[subj.id]
				
	
	def set_sex(self, subject_sex):
		"""
		Set sex for existing subject in cohort.
		
		If subject in dictionary cannot be found, id will be ignored
		
		:param subject_sex (dict): maps subject id to sex
		"""
		
		for subj in self.subjects:
			if subj.id in subject_sex:
				subj.sex = subject_sex[subj.id]
				
	def set_beiwe_ids(self, subject_beiwe_ids):
		"""
		Set beiwe_ids for existing subjects in cohort.
		
		If subject in dictionary cannot be found, id will be ignored
		
		:param subject_beiwe_ids (dict): maps subject id to beiwe_id
		"""
		
		for subj in self.subjects:
			if subj.id in subject_beiwe_ids:
				subj.beiwe_id = subject_beiwe_ids[subj.id]
				
	def column_mean(self, column):
		"""
		Find the mean value for particular domain in cohort
		"""
		col_values = np.concatenate([subj.df[column].values for subj in self.subjects if column in subj.df.columns])
		return np.nanmean(col_values)
				
	def column_stdev(self, column):
		"""
		Find the std value for particular domain in cohort
		"""
		col_values = np.concatenate([subj.df[column].values for subj in self.subjects if column in subj.df.columns])
		return np.nanstd(col_values)
		
	def normalize(self, columns, in_sample=False):
		"""
		Normalize each domain in cohort so that values have 0 mean/unit variance
		
		If in_sample is true, then performs within-sample normalization
		"""
		if in_sample:
			for subj in self.subjects:
				subj.normalize(columns)
		else:
			col_means, col_vars = {col: self.column_mean(col) for col in columns}, {col: self.column_stdev(col) for col in columns}
			
			for subj in self.subjects:
				subj.normalize(columns=columns, col_means=col_means, col_vars=col_vars)
				
	def transition_probabilities(self, columns, joint_size=1):
		"""
		Get cohort_wide transistion probabilities.
		
		:param joint_size (int): the number of variables used when calculating the joint probabilities for transistion event. Defaults to 1. 
		"""
		samples_tp = [pro.get_transitions(columns = columns, joint_size = joint_size) for pro in self]
		
		master_dict = {}
		
		for sample in samples_tp:
			for cat in sample:				
				if cat not in master_dict:
					master_dict[cat] = {state: sample[cat][state] for state in sample[cat]}
				else: #merge
					for state in sample[cat]:
						master_dict[cat][state] = {state2: master_dict[cat][state][state2] + sample[cat][state][state2] for state2 in 
																														master_dict[cat][state]}			
		#Convert to probabilities
		trans_dict = {}
		for cat in master_dict:
			trans_dict[cat] = {}
			for state in master_dict[cat]:
				trans_dict[cat][state] = {}
				for state2 in master_dict[cat][state]:
					if sum(master_dict[cat][state].values()) == 0:
						trans_dict[cat][state][state2] = None
					else:
						trans_dict[cat][state][state2] = float(master_dict[cat][state][state2]) / float(sum(master_dict[cat][state].values()))			
		return trans_dict, master_dict
					
			
		
	
		
		
				
			
					
		
		