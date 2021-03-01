# coding: utf-8

"""
    LAMP Platform

    The LAMP Platform API.

    The version of the OpenAPI document: 1.0.0
    Contact: team@digitalpsych.org
"""


from __future__ import absolute_import

__version__ = "develop"

# import apis into sdk package
from LAMP.api.api_api import APIApi
from LAMP.api.activity_api import ActivityApi
from LAMP.api.activity_event_api import ActivityEventApi
from LAMP.api.activity_spec_api import ActivitySpecApi
from LAMP.api.credential_api import CredentialApi
from LAMP.api.participant_api import ParticipantApi
from LAMP.api.researcher_api import ResearcherApi
from LAMP.api.sensor_api import SensorApi
from LAMP.api.sensor_event_api import SensorEventApi
from LAMP.api.sensor_spec_api import SensorSpecApi
from LAMP.api.study_api import StudyApi
from LAMP.api.type_api import TypeApi

# import ApiClient
from LAMP.api_client import ApiClient

# import Configuration
from LAMP.configuration import Configuration

# import exceptions
from LAMP.exceptions import LAMPException
from LAMP.exceptions import ApiTypeError
from LAMP.exceptions import ApiValueError
from LAMP.exceptions import ApiKeyError
from LAMP.exceptions import ApiException

# import models into sdk package
from LAMP.models.access_citation import AccessCitation
from LAMP.models.activity import Activity
from LAMP.models.activity_event import ActivityEvent
from LAMP.models.activity_spec import ActivitySpec
from LAMP.models.credential import Credential
from LAMP.models.document import Document
from LAMP.models.duration_interval import DurationInterval
from LAMP.models.duration_interval_legacy import DurationIntervalLegacy
from LAMP.models.dynamic_attachment import DynamicAttachment
from LAMP.models.error import Error
from LAMP.models.metadata import Metadata
from LAMP.models.participant import Participant
from LAMP.models.researcher import Researcher
from LAMP.models.sensor import Sensor
from LAMP.models.sensor_event import SensorEvent
from LAMP.models.sensor_spec import SensorSpec
from LAMP.models.study import Study
from LAMP.models.temporal_slice import TemporalSlice

API = APIApi()
Type = TypeApi()
Credential = CredentialApi()
Researcher = ResearcherApi()
Study = StudyApi()
Participant = ParticipantApi()
Activity = ActivityApi()
ActivitySpec = ActivitySpecApi()
ActivityEvent = ActivityEventApi()
Sensor = SensorEventApi()
SensorSpec = SensorEventApi()
SensorEvent = SensorEventApi()

def connect(access_key, secret_key, server_address="api.lamp.digital"):
	client = ApiClient(Configuration(host=f"https://{server_address}", username=access_key, password=secret_key))

	global API
	global Type
	global Credential
	global Researcher
	global Study
	global Participant
	global Activity
	global ActivitySpec
	global ActivityEvent
	global Sensor
	global SensorSpec
	global SensorEvent

	API = APIApi(client)
	Type = TypeApi(client)
	Credential = CredentialApi(client)
	Researcher = ResearcherApi(client)
	Study = StudyApi(client)
	Participant = ParticipantApi(client)
	Activity = ActivityApi(client)
	ActivitySpec = ActivitySpecApi(client)
	ActivityEvent = ActivityEventApi(client)
	Sensor = SensorEventApi(client)
	SensorSpec = SensorEventApi(client)
	SensorEvent = SensorEventApi(client)
