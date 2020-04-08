# LAMP.ActivityEvent


Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_participant**](ActivityEventApi.md#all_by_participant) | **GET** /participant/{participant_id}/activity_event | Get all activity events for a participant.
[**all_by_researcher**](ActivityEventApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/activity_event | Get all activity events for a researcher by participant.
[**all_by_study**](ActivityEventApi.md#all_by_study) | **GET** /study/{study_id}/activity_event | Get all activity events for a study by participant.
[**create**](ActivityEventApi.md#create) | **POST** /participant/{participant_id}/activity_event | Create a new ActivityEvent for the given Participant.
[**delete**](ActivityEventApi.md#delete) | **DELETE** /participant/{participant_id}/activity_event | Delete a ActivityEvent.


# **all_by_participant**
> [object] all_by_participant(participant_id)

Get all activity events for a participant.

Get the set of all activity events produced by a given participant,  by identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str

# Get all activity events for a participant.
result = LAMP.ActivityEvent.all_by_participant(participant_id)
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

Get all activity events for a researcher by participant.

Get the set of all activity events produced by participants of any  study conducted by a researcher, by researcher identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str

# Get all activity events for a researcher by participant.
result = LAMP.ActivityEvent.all_by_researcher(researcher_id)
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

Get all activity events for a study by participant.

Get the set of all activity events produced by participants of a  single study, by study identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str

# Get all activity events for a study by participant.
result = LAMP.ActivityEvent.all_by_study(study_id)
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
> str create(participant_id, activity_event)

Create a new ActivityEvent for the given Participant.

Create a new ActivityEvent for the given Participant.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str
activity_event = LAMP.ActivityEvent() # ActivityEvent | 

# Create a new ActivityEvent for the given Participant.
result = LAMP.ActivityEvent.create(participant_id, activity_event)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
 **activity_event** | [**ActivityEvent**](ActivityEvent.md)|  |

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

Delete a ActivityEvent.

Delete a ActivityEvent.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str

# Delete a ActivityEvent.
result = LAMP.ActivityEvent.delete(participant_id)
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

