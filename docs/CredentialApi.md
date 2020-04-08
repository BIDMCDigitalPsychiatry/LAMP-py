# LAMP.Credential


Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CredentialApi.md#create) | **POST** /type/{type_id}/credential | 
[**delete**](CredentialApi.md#delete) | **DELETE** /type/{type_id}/credential/{access_key} | 
[**list**](CredentialApi.md#list) | **GET** /type/{type_id}/credential | 
[**update**](CredentialApi.md#update) | **PUT** /type/{type_id}/credential/{access_key} | 


# **create**
> bool, date, datetime, dict, float, int, list, str create(type_id, body)



### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str
body = LAMP.Credential()

result = LAMP.Credential.create(type_id, body)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **body** | **bool, date, datetime, dict, float, int, list, str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str**

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
> bool, date, datetime, dict, float, int, list, str delete(type_id, access_key)



### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str
access_key = 'access_key_example' # str

result = LAMP.Credential.delete(type_id, access_key)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **access_key** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str**

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

# **list**
> bool, date, datetime, dict, float, int, list, str list(type_id)



### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str

result = LAMP.Credential.list(type_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

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
> bool, date, datetime, dict, float, int, list, str update(type_id, access_key, body)



### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str
access_key = 'access_key_example' # str
body = LAMP.Credential()

result = LAMP.Credential.update(type_id, access_key, body)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **access_key** | **str**|  |
 **body** | **bool, date, datetime, dict, float, int, list, str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str**

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

