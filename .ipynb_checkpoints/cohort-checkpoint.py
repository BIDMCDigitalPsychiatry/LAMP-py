import lamp
from lamp import cohort_analysis
from functools import reduce
"""
"""

class Cohort():
	"""
	"""
	def __init__(self, subjects):
		self.init_subjects(subjects)
		
		
	def init_subjects(self, subjects):
		self.subjects = []
		for subj in subjects:
			if isinstance(subj, lamp.Subject):
				self.subjects.append(subj)
				
			else:
				try:
					self.add_subject(subj)
					
				except Exception as e:
					print(e)
			
	def add_subject(self, subject):
		self.subjects.append(lamp.Subject(id = subject))
		
	def get_subjects(self):
		"""
		Return all subjects in cohort
		"""
		return self.subjects
	
	
	def get_subjects_age(self):
		"""
		Return mean, std age of subjects in cohort
		"""
		if len(self.subjects) == 0:
			return None
		
		for subj in self.subjects:
			subj.get_age()
			
		return None
		