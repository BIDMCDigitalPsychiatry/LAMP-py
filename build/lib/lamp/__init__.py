import openapi_client 
from subject import Subject
from cohort import Cohort
from survey_question_dict import SurveyQuestionDict

# import apis into sdk package
from openapi_client.api.activity_api import ActivityApi
from openapi_client.api.activity_spec_api import ActivitySpecApi
from openapi_client.api.credential_api import CredentialApi
from openapi_client.api.participant_api import ParticipantApi
from openapi_client.api.researcher_api import ResearcherApi
from openapi_client.api.result_event_api import ResultEventApi
from openapi_client.api.sensor_event_api import SensorEventApi
from openapi_client.api.sensor_spec_api import SensorSpecApi
from openapi_client.api.study_api import StudyApi
from openapi_client.api.type_api import TypeApi


# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiException
# import models into sdk package
from openapi_client.models.access_citation import AccessCitation
from openapi_client.models.activity import Activity
from openapi_client.models.activity_spec import ActivitySpec
from openapi_client.models.credential import Credential
from openapi_client.models.document import Document
from openapi_client.models.duration_interval import DurationInterval
from openapi_client.models.duration_interval_legacy import DurationIntervalLegacy
from openapi_client.models.dynamic_attachment import DynamicAttachment
from openapi_client.models.error import Error
from openapi_client.models.metadata import Metadata
from openapi_client.models.participant import Participant
from openapi_client.models.researcher import Researcher
from openapi_client.models.result_event import ResultEvent
from openapi_client.models.sensor_event import SensorEvent
from openapi_client.models.sensor_spec import SensorSpec
from openapi_client.models.study import Study
from openapi_client.models.temporal_event import TemporalEvent

HOST = "https://api.lamp.digital"
KEY = "TESTCREDENTIALS" # your login credentials go here
BETA_VALUES_FILEPATH = "BETA_FILEPATH" #filepath to folder holding beta values


configuration = Configuration(host = HOST)
configuration.api_key['Authorization'] = KEY
configuration.api_key_ppwdrefix['Authorization'] = 'Basic'


activity = ActivityApi(ApiClient(configuration))
activity_spec = ActivitySpecApi(ApiClient(configuration))
credential = CredentialApi(ApiClient(configuration))
participant = ParticipantApi(ApiClient(configuration))
researcher = ResearcherApi(ApiClient(configuration))
result_event = ResultEventApi(ApiClient(configuration))
sensor_event = SensorEventApi(ApiClient(configuration))
study = StudyApi(ApiClient(configuration))
type = TypeApi(ApiClient(configuration))
