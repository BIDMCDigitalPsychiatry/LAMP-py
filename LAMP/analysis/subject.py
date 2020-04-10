import pandas as pd 
import numpy as np
import datetime
import os
import math
import LAMP
import itertools
from functools import reduce
#import

class Subject():
    """
    Create subject dataframe


    """
    def __init__(self, 
                 id, 
                 domains=None, 
                 age=None, 
                 race=None, 
                 sex=None, 
                 beiwe_id=None, 
                 beiwe_filepath=None, 
                 beta_values_filepath=None,
                 df_props={}):

        self.id = id
        self.domains = domains
        self.beiwe_id = beiwe_id
        self.beiwe_filepath = beiwe_filepath
        self.beta_values_filepath = beta_values_filepath
        self.age = age
        self.race = race
        self.sex = sex

        self.df = self.create_subject_df(**df_props)

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
    
    @property
    def beta_values_filepath(self):
        return self._beta_values_filepath

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
        
    @beta_values_filepath.setter
    def beta_values_filepath(self, value):
        self._beta_values_filepath = value

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


    def survey_results(self, participant=None, question_categories=None):
        """
        Get survey events for participant

        :param participant (str): the LAMP ID for participant. If not provided, then take subjects
        :param question_categories (bool): indicates whether to use custom question mappings as defined in params file
        """
        def survey_results_with_custom_categories(participant_results, question_categories):
            """
            """

            participant_surveys = {}
            for result in participant_results:
                survey_time = result['timestamp']

                #Parse survey event with defined questions
                survey_result = {}
                for event in result['temporal_slices']:
                    question = event['item']                    
                    if question in question_categories: #Check if question in one of the categories
                        score = int(event['value'])
                        if question_categories[question]['category']['reverse_scoring']:
                            score = 3 - score 
                        category = question_categories[question]['category']
                        if category in survey_result: survey_result[category].append(score) 
                        else: survey_result[category] = [score]

                #Take mean for each cat
                for cat in survey_result:
                    survey_result[cat] = float(sum(survey_result[cat])/len(survey_result[cat]))
                
                for category in survey_result: #Add to master dictionary
                    if category not in participant_surveys: participant_surveys[category] = [(survey_result[category], survey_time)]
                    else: participant_surveys[category].append((survey_result[category], survey_time))

            return participant_surveys


        if participant is None:
            participant = self.id
            

        participant_activities = LAMP.Activity.all_by_participant(participant)['data']
        participant_activities_surveys = [activity for activity in participant_activities if activity['spec'] == 'lamp.survey']
        participant_activities_surveys_ids = [survey['id'] for survey in participant_activities_surveys]        
        
        participant_results = [result for result in LAMP.ActivityEvent.all_by_participant(participant)['data'] if result['activity'] in participant_activities_surveys_ids and len(result['temporal_slices']) > 0]

        #Perform different parsing if user-defined question categories
        if question_categories:
            return survey_results_with_custom_categories(participant_results, question_categories)

        participant_surveys = {} #maps survey_type to occurence of scores 
        for result in participant_results:

            #Check if it's a survey event
            if result['activity'] not in participant_activities_surveys_ids or len(result['temporal_slices']) == 0: continue
            activity = LAMP.Activity.view(result['activity'])['data'][0]
            
            #Check to see if all the event values are numerical
            try: [float(event['value']) for event in result['temporal_slices']]
            except: continue
                
            survey_time = result['timestamp']
            survey_score = sum([float(event['value']) for event in result['temporal_slices']]) / len(result['temporal_slices'])
            
            #Add result
            if activity['name'] not in participant_surveys:
                participant_surveys[activity['name']] = []
            participant_surveys[activity['name']].append((survey_score, survey_time))
          
        return participant_surveys

    def create_subject_df(self, days_cap=120, day_first=None, day_last=None, resolution='day', start_monday=False, start_morning=True, time_centered=False, question_categories=None):
        """
        Create subject dataframe

        :param day_first (datetime.Date)
        """

        FIFTEEN_MIN_PER_UNIT = {'15 min': 1, 'day': 4*24, 'week': 4*24*7, 'month': 4*24*30}
        UNITS_PER_DAY = {'15 min': 4*24, 'day': 1, 'week': 1/7, 'month': 1/30}

        def parse_surveys(days_cap=120, day_first=None, day_last=None, resolution='day', start_monday=False, start_morning=True, time_centered=False, question_categories=None):            
            subject_surveys = self.survey_results(question_categories=question_categories)
            if len(subject_surveys) == 0:
                return None
            
            #Find the first, last date
            if day_first is None: day_first = datetime.datetime.utcfromtimestamp(sorted([subject_surveys[dom][0][1]/1000 for dom in subject_surveys])[0])
            else: day_first = datetime.datetime.combine(day_first, datetime.time.min) #convert to datetime

            if day_last is None: day_last = datetime.datetime.utcfromtimestamp(sorted([subject_surveys[dom][-1][1]/1000 for dom in subject_surveys])[-1])
            else: day_first = datetime.datetime.combine(day_first, datetime.time.min) #convert to datetime

            #Clip days based on morning and weekday parameters
            if start_monday:
                if day_first.weekday() > 0: 
                    day_first += datetime.timedelta(days = - day_first.weekday())

            if start_morning: 
                day_first, day_last = day_first.replace(hour=9, minute=0, second=0), day_last.replace(hour=9, minute=0, second=0)
            days_elapsed = (day_last - day_first).days 
            date_list = [day_first + datetime.timedelta(minutes=15*FIFTEEN_MIN_PER_UNIT[resolution]*x) for x in range(0, math.ceil(min(days_elapsed, days_cap) * UNITS_PER_DAY[resolution]))]

            #Create dateframe for the number of time units that have data; limited by days; cap at 'days_cap' if this number is large
            df = pd.DataFrame({'Date': date_list, 'id':self.id})
            
            if self.domains is None: domains = [dom for dom in subject_surveys] #if not set, just use cats from surveys
            else: domains = self.domains
            for dom in domains: 
                df[dom] = np.nan

            #Parse surveys
            for dom in subject_surveys:
                if dom not in domains and domains is not None:
                    continue

                #Based on resolution, match each survey event to its closest date
                dates = [datetime.datetime.utcfromtimestamp(event_time/1000) for _, event_time in subject_surveys[dom] if day_first <= datetime.datetime.utcfromtimestamp(event_time/1000) <= day_last] 

                #Choose closest date if "time centered"; else, choose preceding date
                if time_centered: rounded_dates = [df.loc[df.index[(date - df['Date']).abs().sort_values().index[0]], 'Date'] for date in dates]
                else: rounded_dates = [df.loc[df.index[(date - df['Date'])[(date - df['Date']) >= datetime.timedelta(0)].sort_values().index[0]], 'Date'] for date in dates]

                results = [event_val for event_val, event_time in subject_surveys[dom] if day_first <= datetime.datetime.utcfromtimestamp(event_time/1000) <= day_last]
                dom_results = pd.DataFrame({'Date':dates, 'Rounded Date':rounded_dates, 'Result':results})
                for date, date_df in dom_results.groupby('Rounded Date'):                    
                    df.loc[df['Date'] == date.to_pydatetime(), dom] = np.mean(date_df['Result']) 
    
            #Convert to date to actual date objects if resolution is day or greater
            if resolution != '15 min':
                df['Date'] = df['Date'].apply(lambda d: d.date())
            return df

        
        def parse_beta_values(days_cap=120):
            """
            """
            if self.beta_values_filepath is None: return None
            beta_val_list = pd.read_csv(self.beta_values_filepath)
            beta_val_list['Date'] = pd.to_datetime(beta_val_list['date'])
            subj_beta_vals = beta_val_list.loc[beta_val_list['id'] == self.id]
            if subj_beta_vals.empty: return subj_beta_vals[['Date', 'beta_a', 'beta_b']]
            first_date = subj_beta_vals.iloc[0]['Date']
            return subj_beta_vals.loc[(subj_beta_vals['Date'] >= first_date) & (subj_beta_vals['Date'] < first_date + datetime.timedelta(days=days_cap)), ['Date', 'beta_a', 'beta_b']]


        def parse_beiwe_pipeline(days_cap=120):
            """
            """
            #Find beiwe id
            if self.beiwe_filepath is None:
                return None, None 
            
            if not isinstance(self.beiwe_id, str):                
                return None, None 

            steps_file, sleep_file = None, None
            #Get step data
            if os.path.exists(os.path.join(self.beiwe_filepath, self.beiwe_id, 'steps.csv')):
                steps_file = pd.read_csv(os.path.join(self.beiwe_filepath, self.beiwe_id, 'steps.csv'))
                steps_file['Date'] = pd.to_datetime(steps_file['Date'], format='%Y-%m-%d')
                if steps_file.empty: pass
                else: steps_file = steps_file.loc[(steps_file['Date'] >= steps_file.iloc[0]['Date']) & (steps_file['Date'] < steps_file.iloc[0]['Date'] + datetime.timedelta(days=days_cap))]

            #Get sleep_data
            if os.path.exists(os.path.join(self.beiwe_filepath, self.beiwe_id, 'sleep_estimates.csv')):
                sleep_file = pd.read_csv(os.path.join(self.beiwe_filepath, self.beiwe_id, 'sleep_estimates.csv'))
                sleep_file['Date'] = pd.to_datetime(sleep_file['Date'], format='%Y-%m-%d')
                if sleep_file.empty: pass
                else: sleep_file = sleep_file.loc[(sleep_file['Date'] >= sleep_file.iloc[0]['Date']) & (sleep_file['Date'] < sleep_file.iloc[0]['Date'] + datetime.timedelta(days=days_cap))]

            return steps_file, sleep_file
 
        assert resolution in ['15 min', 'day', 'week', 'month']


        surveys = parse_surveys(days_cap=days_cap, 
                                day_first=day_first, 
                                day_last=day_last, 
                                resolution=resolution, 
                                start_monday=start_monday, 
                                start_morning=start_morning, 
                                time_centered=time_centered,
                                question_categories=question_categories)

        beta_vals = parse_beta_values(days_cap=days_cap)
        steps_file, sleep_file = parse_beiwe_pipeline(days_cap=days_cap)
        dataframes = [d for d in [surveys, beta_vals, steps_file, sleep_file] if d is not None] 
        if len(dataframes) == 0:
            df_final = pd.DataFrame({})
        else:
            df_final = reduce(lambda left,right: pd.merge(left, right, on='Date', how='outer'), dataframes).sort_values(by=['Date'])

        #Set domains
        #if self.domains is None: self.domains = [col for col in df_final.columns if col not in ['Date', 'id']]

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


    def bin(self, domains, window_size=3, shift=0):
        """
        Bin dataframe

        :param domains (list): the domains to bin 
        :window_size (int): the size of the bins (in days)
        :shift (int): the day of the week to start the binning on (Monday == 0)

        """

        domains = self.domain_check(domains)
        #Shift until Monday
        df_copy = self.df.copy()
        if shift is not None:
            try:
                dow = df_copy.iloc[0]['Date'].weekday()
                if dow > 0 and len(df_copy) > dow:
                    df_copy = df_copy.shift(shift - dow)
            except:
                print(self.id, df_copy)
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
        
    def impute_bins(self, domains):
        """
        Try to impute bin objects
        """
        assert self.bins is not None
        
        for d in domains:
            for index, row in self.bins.iterrows():
                if 0 < index < len(self.bins.index) - 1:
                    index = int(index)
                    if pd.isnull(self.bins.iloc[index][d]) and not pd.isnull(self.bins.iloc[index-1][d]) and not pd.isnull(self.bins.iloc[index+1][d]):                        
                        self.bins.at[index,d] = np.mean([self.bins.iloc[index-1][d], self.bins.iloc[index+1][d]])


    def normalize(self, domains, domain_means={}, domain_vars={}):
        """
        Normalize columns values to 0 mean/ unit variance
        :param domain_means (dict): the mean for each column value
        :param domain_vars (dict): the variance for each column value

        If mean/var not provided, resort to in-sample normalization
        """
        if self.normalize_status:
            #print("Dataframe has already been normalized. Please reset dataframe if you wish to normalize it in a different way.")
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

