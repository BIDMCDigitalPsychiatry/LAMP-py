# LAMP.Study


Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](StudyApi.md#all) | **GET** /study | Get the set of all studies.
[**all_by_researcher**](StudyApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/study | Get the set of studies for a single researcher.
[**create**](StudyApi.md#create) | **POST** /researcher/{researcher_id}/study | Create a new Study for the given Researcher.
[**delete**](StudyApi.md#delete) | **DELETE** /study/{study_id} | Delete a study.
[**update**](StudyApi.md#update) | **PUT** /study/{study_id} | Update the study.
[**view**](StudyApi.md#view) | **GET** /study/{study_id} | Get a single study, by identifier.


# **all**
> [object] all()

Get the set of all studies.

Get the set of all studies.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

# Get the set of all studies.
result = LAMP.Study.all()
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

Get the set of studies for a single researcher.

Get the set of studies for a single researcher.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str

# Get the set of studies for a single researcher.
result = LAMP.Study.all_by_researcher(researcher_id)
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

# **create**
> str create(researcher_id, study)

Create a new Study for the given Researcher.

Create a new Study for the given Researcher.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str
study = LAMP.Study() # Study | 

# Create a new Study for the given Researcher.
result = LAMP.Study.create(researcher_id, study)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_id** | **str**|  |
 **study** | [**Study**](Study.md)|  |

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
> str delete(study_id)

Delete a study.

Delete a study.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str

# Delete a study.
result = LAMP.Study.delete(study_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |

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
> str update(study_id, study)

Update the study.

Update the study.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str
study = LAMP.Study() # Study | 

# Update the study.
result = LAMP.Study.update(study_id, study)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
 **study** | [**Study**](Study.md)|  |

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
> [object] view(study_id)

Get a single study, by identifier.

Get a single study, by identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str

# Get a single study, by identifier.
result = LAMP.Study.view(study_id)
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

