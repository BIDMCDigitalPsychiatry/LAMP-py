# LAMP.Researcher


Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](ResearcherApi.md#all) | **GET** /researcher | Get the set of all researchers.
[**create**](ResearcherApi.md#create) | **POST** /researcher | Create a new Researcher.
[**delete**](ResearcherApi.md#delete) | **DELETE** /researcher/{researcher_id} | Delete a researcher.
[**update**](ResearcherApi.md#update) | **PUT** /researcher/{researcher_id} | Update a Researcher&#39;s settings.
[**view**](ResearcherApi.md#view) | **GET** /researcher/{researcher_id} | Get a single researcher, by identifier.


# **all**
> [object] all()

Get the set of all researchers.

Get the set of all researchers.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

# Get the set of all researchers.
result = LAMP.Researcher.all()
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

# **create**
> str create(researcher_researcher)

Create a new Researcher.

Create a new Researcher.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_researcher = LAMP.Researcher() # Researcher

# Create a new Researcher.
result = LAMP.Researcher.create(researcher_researcher)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_researcher** | [**Researcher**](Researcher.md)|  |

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
> str delete(researcher_id)

Delete a researcher.

Delete a researcher.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str

# Delete a researcher.
result = LAMP.Researcher.delete(researcher_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_id** | **str**|  |

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
> str update(researcher_id, researcher_researcher)

Update a Researcher's settings.

Update a Researcher's settings.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str
researcher_researcher = LAMP.Researcher() # Researcher

# Update a Researcher's settings.
result = LAMP.Researcher.update(researcher_id, researcher_researcher)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_id** | **str**|  |
 **researcher_researcher** | [**Researcher**](Researcher.md)|  |
 **transform** | **str**|  | [optional]

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
> [object] view(researcher_id)

Get a single researcher, by identifier.

Get a single researcher, by identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str

# Get a single researcher, by identifier.
result = LAMP.Researcher.view(researcher_id)
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

