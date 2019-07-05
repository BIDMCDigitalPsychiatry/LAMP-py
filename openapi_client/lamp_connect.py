import openapi_client
from openapi_client.rest import ApiException

class LAMP_CONN():
	"""
	Object that stores all connections to various LAMP API objects
	"""
	def __init__(self, host, api_key):
		configuration = openapi_client.Configuration()
		configuration.host = host
		configuration.api_key['Authorization'] = api_key
		configuration.api_key_prefix['Authorization'] = 'Basic'
		self.configuration = configuration
		def create_connections():
		#Create class attributes of containing static methods
			self.activity = openapi_client.ActivityApi(openapi_client.ApiClient(self.configuration))
			self.activity_spec = openapi_client.ActivitySpecApi(openapi_client.ApiClient(self.configuration))
			self.environment_event = openapi_client.EnvironmentEventApi(openapi_client.ApiClient(self.configuration))
			self.fitness_event = openapi_client.FitnessEventApi(openapi_client.ApiClient(self.configuration))
			self.metadata_event = openapi_client.MetadataEventApi(openapi_client.ApiClient(self.configuration))
			self.participant = openapi_client.ParticipantApi(openapi_client.ApiClient(self.configuration))
			self.researcher = openapi_client.ResearcherApi(openapi_client.ApiClient(self.configuration))
			self.result_event = openapi_client.ResultEventApi(openapi_client.ApiClient(self.configuration))
			self.sensor_event = openapi_client.SensorEventApi(openapi_client.ApiClient(self.configuration))
			self.study = openapi_client.StudyApi(openapi_client.ApiClient(self.configuration))
			self.type = openapi_client.TypeApi(openapi_client.ApiClient(self.configuration))
			self.type_legacy = openapi_client.TypeLegacyApi(openapi_client.ApiClient(self.configuration))

		create_connections()