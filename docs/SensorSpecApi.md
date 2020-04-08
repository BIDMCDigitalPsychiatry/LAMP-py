# LAMP.SensorSpec


Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](SensorSpecApi.md#all) | **GET** /sensor_spec | Get all SensorSpecs registered.
[**create**](SensorSpecApi.md#create) | **POST** /sensor_spec | Create a new SensorSpec.
[**delete**](SensorSpecApi.md#delete) | **DELETE** /sensor_spec/{sensor_spec_name} | Delete an SensorSpec.
[**update**](SensorSpecApi.md#update) | **PUT** /sensor_spec/{sensor_spec_name} | Update an SensorSpec.
[**view**](SensorSpecApi.md#view) | **GET** /sensor_spec/{sensor_spec_name} | Get a SensorSpec.


# **all**
> [object] all()

Get all SensorSpecs registered.

Get all SensorSpecs registered by any Researcher.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

# Get all SensorSpecs registered.
result = LAMP.SensorSpec.all()
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
> str create(sensor_spec)

Create a new SensorSpec.

Create a new SensorSpec.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

sensor_spec = LAMP.SensorSpec() # SensorSpec

# Create a new SensorSpec.
result = LAMP.SensorSpec.create(sensor_spec)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_spec** | [**SensorSpec**](SensorSpec.md)|  |

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
> str delete(sensor_spec_name)

Delete an SensorSpec.

Delete an SensorSpec.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

sensor_spec_name = 'sensor_spec_name_example' # str

# Delete an SensorSpec.
result = LAMP.SensorSpec.delete(sensor_spec_name)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_spec_name** | **str**|  |

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
> str update(sensor_spec_name, sensor_spec)

Update an SensorSpec.

Update an SensorSpec.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

sensor_spec_name = 'sensor_spec_name_example' # str
sensor_spec = LAMP.SensorSpec() # SensorSpec

# Update an SensorSpec.
result = LAMP.SensorSpec.update(sensor_spec_name, sensor_spec)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_spec_name** | **str**|  |
 **sensor_spec** | [**SensorSpec**](SensorSpec.md)|  |

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
> [object] view(sensor_spec_name)

Get a SensorSpec.

Get a SensorSpec.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

sensor_spec_name = 'sensor_spec_name_example' # str

# Get a SensorSpec.
result = LAMP.SensorSpec.view(sensor_spec_name)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_spec_name** | **str**|  |
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

