# LAMP.ActivitySpec


Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](ActivitySpecApi.md#all) | **GET** /activity_spec | Get all ActivitySpecs registered.
[**create**](ActivitySpecApi.md#create) | **POST** /activity_spec | Create a new ActivitySpec.
[**delete**](ActivitySpecApi.md#delete) | **DELETE** /activity_spec/{activity_spec_name} | Delete an ActivitySpec.
[**update**](ActivitySpecApi.md#update) | **PUT** /activity_spec/{activity_spec_name} | Update an ActivitySpec.
[**view**](ActivitySpecApi.md#view) | **GET** /activity_spec/{activity_spec_name} | View an ActivitySpec.


# **all**
> [object] all()

Get all ActivitySpecs registered.

Get all ActivitySpecs registered.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

# Get all ActivitySpecs registered.
result = LAMP.ActivitySpec.all()
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
> str create(activity_spec)

Create a new ActivitySpec.

Create a new ActivitySpec.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

activity_spec = LAMP.ActivitySpec() # ActivitySpec | 

# Create a new ActivitySpec.
result = LAMP.ActivitySpec.create(activity_spec)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_spec** | [**ActivitySpec**](ActivitySpec.md)|  |

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
> str delete(activity_spec_name)

Delete an ActivitySpec.

Delete an ActivitySpec.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

activity_spec_name = 'activity_spec_name_example' # str

# Delete an ActivitySpec.
result = LAMP.ActivitySpec.delete(activity_spec_name)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_spec_name** | **str**|  |

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
> str update(activity_spec_name, activity_spec)

Update an ActivitySpec.

Update an ActivitySpec.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

activity_spec_name = 'activity_spec_name_example' # str
activity_spec = LAMP.ActivitySpec() # ActivitySpec

# Update an ActivitySpec.
result = LAMP.ActivitySpec.update(activity_spec_name, activity_spec)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_spec_name** | **str**|  |
 **activity_spec** | [**ActivitySpec**](ActivitySpec.md)|  |

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
> str view(activity_spec_name)

View an ActivitySpec.

View an ActivitySpec.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

activity_spec_name = 'activity_spec_name_example' # str

# View an ActivitySpec.
result = LAMP.ActivitySpec.view(activity_spec_name)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_spec_name** | **str**|  |
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

