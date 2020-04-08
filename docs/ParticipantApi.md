# LAMP.Participant


Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](ParticipantApi.md#all) | **GET** /participant | Get the set of all participants.
[**all_by_researcher**](ParticipantApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/participant | Get the set of all participants under a single researcher.
[**all_by_study**](ParticipantApi.md#all_by_study) | **GET** /study/{study_id}/participant | Get the set of all participants in a single study.
[**create**](ParticipantApi.md#create) | **POST** /study/{study_id}/participant | Create a new Participant for the given Study.
[**delete**](ParticipantApi.md#delete) | **DELETE** /participant/{participant_id} | Delete a participant AND all owned data or event streams.
[**update**](ParticipantApi.md#update) | **PUT** /participant/{participant_id} | Update a Participant&#39;s settings.
[**view**](ParticipantApi.md#view) | **GET** /participant/{participant_id} | Get a single participant, by identifier.


# **all**
> [object] all()

Get the set of all participants.

Get the set of all participants.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

# Get the set of all participants.
result = LAMP.Participant.all()
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

Get the set of all participants under a single researcher.

Get the set of all participants under a single researcher.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str

# Get the set of all participants under a single researcher.
result = LAMP.Participant.all_by_researcher(researcher_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_id** | **str**|  |
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

Get the set of all participants in a single study.

Get the set of all participants in a single study.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str

# Get the set of all participants in a single study.
result = LAMP.Participant.all_by_study(study_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
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
> str create(study_id, participant)

Create a new Participant for the given Study.

Create a new Participant for the given Study.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str
participant = LAMP.Participant() # Participant

# Create a new Participant for the given Study.
result = LAMP.Participant.create(study_id, participant)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
 **participant** | [**Participant**](Participant.md)|  |

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

Delete a participant AND all owned data or event streams.

Delete a participant AND all owned data or event streams.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str

# Delete a participant AND all owned data or event streams.
result = LAMP.Participant.delete(participant_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |

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

# **update**
> str update(participant_id, participant)

Update a Participant's settings.

Update a Participant's settings.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str
participant = LAMP.Participant() # Participant

# Update a Participant's settings.
result = LAMP.Participant.update(participant_id, participant)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
 **participant** | [**Participant**](Participant.md)|  |

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

# **view**
> [object] view(participant_id)

Get a single participant, by identifier.

Get a single participant, by identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str

# Get a single participant, by identifier.
result = LAMP.Participant.view(participant_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
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

