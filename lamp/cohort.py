import lamp
import numpy as np
from lamp import cohort_analysis
from functools import reduce
"""
"""

class Cohort():
	"""
	"""
	def __init__(self, subjects, ages=None, races=None, sex=None):
		self.init_subjects(subjects)
		if ages is not None:
			self.set_ages(ages)
		if races is not None:
			self.set_races(races)
		if sex is not None:
			self.set_sex(sex)
			
			
		
		
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
			if subj.get_id() == subj_id:
				return subj
		
		print('Subject not found!')
		return None
	
	def add_subject(self, subject):
		self.subjects.append(lamp.Subject(id = subject))
		
	def get_subjects(self):
		"""
		Return all subjects in cohort
		"""
		return self.subjects
	
	
	def get_mean_age(self):
		"""
		Return mean, std age of subjects in cohort
		"""
		subject_ages = [subj.get_age() for subj in self.subjects if subj.get_age() is not None]
		if len(subject_ages) == 0:
			return None
		
		return np.mean(subject_ages)

	
	def get_std_age(self):
		"""
		Return std age of subjects in cohort
		"""
		subject_ages = [subj.get_age() for subj in self.subjects if subj.get_age() is not None]
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
			if subj.get_id() in subject_ages:
				subj.set_age(age=subject_ages[subj.get_id()])
				
				
	def set_races(self, subject_races):
		"""
		Set race for existing subject in cohort.
		
		If subject in dictionary cannot be found, id will be ignored
		
		:param subject_races (dict): maps subject id to race
		"""
		
		for subj in self.subjects:
			if subj.get_id() in subject_races:
				subj.set_race(race=subject_races[subj.get_id()])
				
	
	def set_sex(self, subject_sex):
		"""
		Set sex for existing subject in cohort.
		
		If subject in dictionary cannot be found, id will be ignored
		
		:param subject_ages (dict): maps subject id to sex
		"""
		
		for subj in self.subjects:
			if subj.get_id() in subject_sex:
				subj.set_sex(sex=subject_sex[subj.get_id()])
				
	def get_column_mean(self, column):
		"""
		Find the mean value for particular domain in cohort
		"""
		col_values = np.concatenate([subj.df[column].values for subj in self.subjects if column in subj.df.columns])
		return np.nanmean(col_values)
				
	def get_column_stdev(self, column):
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
			col_means, col_vars = {col: self.get_column_mean(col) for col in columns}, {col: self.get_column_stdev(col) for col in columns}
			
			for subj in self.subjects:
				subj.normalize(columns=columns, col_means=col_means, col_vars=col_vars)
				
	
		
		
				
			
					
		
		