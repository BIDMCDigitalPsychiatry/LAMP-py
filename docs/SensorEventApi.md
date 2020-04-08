# LAMP.SensorEvent


Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_participant**](SensorEventApi.md#all_by_participant) | **GET** /participant/{participant_id}/sensor_event | Get all sensor events for a participant.
[**all_by_researcher**](SensorEventApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/sensor_event | Get all sensor events for a researcher by participant.
[**all_by_study**](SensorEventApi.md#all_by_study) | **GET** /study/{study_id}/sensor_event | Get all sensor events for a study by participant.
[**create**](SensorEventApi.md#create) | **POST** /participant/{participant_id}/sensor_event | Create a new SensorEvent for the given Participant.
[**delete**](SensorEventApi.md#delete) | **DELETE** /participant/{participant_id}/sensor_event | Delete a sensor event.


# **all_by_participant**
> [object] all_by_participant(participant_id)

Get all sensor events for a participant.

Get the set of all sensor events produced by the given participant.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str

# Get all sensor events for a participant.
result = LAMP.SensorEvent.all_by_participant(participant_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
 **origin** | **str**|  | [optional]
 **_from** | **float**|  | [optional]
 **to** | **float**|  | [optional]
 **transform** | **str**|  | [optional]

### Return type

**[object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_by_researcher**
> [object] all_by_researcher(researcher_id)

Get all sensor events for a researcher by participant.

Get the set of all sensor events produced by participants of any  study conducted by a researcher, by researcher identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str

# Get all sensor events for a researcher by participant.
result = LAMP.SensorEvent.all_by_researcher(researcher_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_id** | **str**|  |
 **origin** | **str**|  | [optional]
 **_from** | **float**|  | [optional]
 **to** | **float**|  | [optional]
 **transform** | **str**|  | [optional]

### Return type

**[object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_by_study**
> [object] all_by_study(study_id)

Get all sensor events for a study by participant.

Get the set of all sensor events produced by participants of a  single study, by study identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str

# Get all sensor events for a study by participant.
result = LAMP.SensorEvent.all_by_study(study_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
 **origin** | **str**|  | [optional]
 **_from** | **float**|  | [optional]
 **to** | **float**|  | [optional]
 **transform** | **str**|  | [optional]

### Return type

**[object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> str create(participant_id, sensor_event)

Create a new SensorEvent for the given Participant.

Create a new SensorEvent for the given Participant.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str
sensor_event = LAMP.SensorEvent() # SensorEvent

# Create a new SensorEvent for the given Participant.
result = LAMP.SensorEvent.create(participant_id, sensor_event)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
 **sensor_event** | [**SensorEvent**](SensorEvent.md)|  |

### Return type

**str**

### HTTP request headers

 - **Content-Type**: `application/json`
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> str delete(participant_id)

Delete a sensor event.

Delete a sensor event.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str

# Delete a sensor event.
result = LAMP.SensorEvent.delete(participant_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
 **origin** | **str**|  | [optional]
 **_from** | **float**|  | [optional]
 **to** | **float**|  | [optional]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

