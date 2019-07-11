import openapi_client 
import cohort_analysis
from subject import Subject
from cohort import Cohort
from survey_question_dict import SurveyQuestionDict

HOST = "https://api.lamp.digital"
KEY = "root:lampadmin" # your login credentials go here

configuration = openapi_client.Configuration()
configuration.host = HOST
configuration.api_key['Authorization'] = KEY
configuration.api_key_prefix['Authorization'] = 'Basic'


activity = openapi_client.ActivityApi(openapi_client.ApiClient(configuration))
activity_spec = openapi_client.ActivitySpecApi(openapi_client.ApiClient(configuration))
environment_event = openapi_client.EnvironmentEventApi(openapi_client.ApiClient(configuration))
fitness_event = openapi_client.FitnessEventApi(openapi_client.ApiClient(configuration))
metadata_event = openapi_client.MetadataEventApi(openapi_client.ApiClient(configuration))
participant = openapi_client.ParticipantApi(openapi_client.ApiClient(configuration))
researcher = openapi_client.ResearcherApi(openapi_client.ApiClient(configuration))
result_event = openapi_client.ResultEventApi(openapi_client.ApiClient(configuration))
sensor_event = openapi_client.SensorEventApi(openapi_client.ApiClient(configuration))
study = openapi_client.StudyApi(openapi_client.ApiClient(configuration))
type = openapi_client.TypeApi(openapi_client.ApiClient(configuration))
type_legacy = openapi_client.TypeLegacyApi(openapi_client.ApiClient(configuration))

#subject_data = SubjectDataframe


