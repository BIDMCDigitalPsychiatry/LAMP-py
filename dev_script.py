import lamp


def resolution_test(subj, res):
	test_subj.df = test_subj.create_subject_df(resolution=res, start_monday=True, question_categories=True)
	print(res, '\n', test_subj.df)#[test_subj.df['Anxiety'].notnull()])

if __name__ == '__main__':

	lamp.configure(username="admin", password="LAMPLAMP")
	test_subj = lamp.Subject(id='U1684566141')
	test_subj.domains = None

	#Resolution functionality
	for res in ['15 min', 'day', 'week', 'month']: 
		resolution_test(test_subj, res)
