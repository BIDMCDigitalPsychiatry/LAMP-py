# LAMP.Activity


Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](ActivityApi.md#all) | **GET** /activity | Get the set of all activities.
[**all_by_participant**](ActivityApi.md#all_by_participant) | **GET** /participant/{participant_id}/activity | Get all activities for a participant.
[**all_by_researcher**](ActivityApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/activity | Get all activities for a researcher.
[**all_by_study**](ActivityApi.md#all_by_study) | **GET** /study/{study_id}/activity | Get all activities in a study.
[**create**](ActivityApi.md#create) | **POST** /study/{study_id}/activity | Create a new Activity under the given Study.
[**delete**](ActivityApi.md#delete) | **DELETE** /activity/{activity_id} | Delete an Activity.
[**update**](ActivityApi.md#update) | **PUT** /activity/{activity_id} | Update an Activity&#39;s settings.
[**view**](ActivityApi.md#view) | **GET** /activity/{activity_id} | Get a single activity, by identifier.


# **all**
> [object] all()

Get the set of all activities.

Get the set of all activities.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

# Get the set of all activities.
result = LAMP.Activity.all()
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

# **all_by_participant**
> [object] all_by_participant(participant_id)

Get all activities for a participant.

Get the set of all activities available to a participant, by  participant identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str 

# Get all activities for a participant.
result = LAMP.Activity.all_by_participant(participant_id)
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

# **all_by_researcher**
> [object] all_by_researcher(researcher_id)

Get all activities for a researcher.

Get the set of all activities available to participants of any study  conducted by a researcher, by researcher identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str

# Get all activities for a researcher.
result = LAMP.Activity.all_by_researcher(researcher_id)
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

Get all activities in a study.

Get the set of all activities available to  participants of a single  study, by study identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str

# Get all activities in a study.
result = LAMP.Activity.all_by_study(study_id)
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
> str create(study_id, activity)

Create a new Activity under the given Study.

Create a new Activity under the given Study.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str 
activity = LAMP.Activity() # Activity 

# Create a new Activity under the given Study.
result = LAMP.Activity.create(study_id, activity)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
 **activity** | [**Activity**](Activity.md)|  |

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
> str delete(activity_id)

Delete an Activity.

Delete an Activity.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

activity_id = 'activity_id_example' # str

# Delete an Activity.
result = LAMP.Activity.delete(activity_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  |

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
> str update(activity_id, activity)

Update an Activity's settings.

Update an Activity's settings.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

activity_id = 'activity_id_example' # str 
activity = LAMP.Activity() # Activity

# Update an Activity's settings.
result = LAMP.Activity.update(activity_id, activity)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  |
 **activity** | [**Activity**](Activity.md)|  |

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
> [object] view(activity_id)

Get a single activity, by identifier.

Get a single activity, by identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

activity_id = 'activity_id_example' # str

# Get a single activity, by identifier.
result = LAMP.Activity.view(activity_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  |
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

