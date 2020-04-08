# LAMP.Type


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attachment**](TypeApi.md#get_attachment) | **GET** /type/{type_id}/attachment/{attachment_key} | 
[**get_dynamic_attachment**](TypeApi.md#get_dynamic_attachment) | **GET** /type/{type_id}/attachment/dynamic/{attachment_key} | 
[**list_attachments**](TypeApi.md#list_attachments) | **GET** /type/{type_id}/attachment | 
[**parent**](TypeApi.md#parent) | **GET** /type/{type_id}/parent | Find the owner(s) of the resource.
[**set_attachment**](TypeApi.md#set_attachment) | **PUT** /type/{type_id}/attachment/{attachment_key}/{target} | 
[**set_dynamic_attachment**](TypeApi.md#set_dynamic_attachment) | **PUT** /type/{type_id}/attachment/dynamic/{attachment_key}/{target} | 


# **get_attachment**
> bool, date, datetime, dict, float, int, list, str get_attachment(type_id, attachment_key)



### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str
attachment_key = 'attachment_key_example' # str

result = LAMP.Type.get_attachment(type_id, attachment_key)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **attachment_key** | **str**|  |

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

# **get_dynamic_attachment**
> bool, date, datetime, dict, float, int, list, str get_dynamic_attachment(type_id, attachment_key, invoke_always, include_logs, ignore_output)



### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str
attachment_key = 'attachment_key_example' # str
invoke_always = True # bool
include_logs = True # bool
ignore_output = True # bool

result = LAMP.Type.get_dynamic_attachment(type_id, attachment_key, invoke_always, include_logs, ignore_output)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **attachment_key** | **str**|  |
 **invoke_always** | **bool**|  |
 **include_logs** | **bool**|  |
 **ignore_output** | **bool**|  |

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

# **list_attachments**
> bool, date, datetime, dict, float, int, list, str list_attachments(type_id)



### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str

result = LAMP.Type.list_attachments(type_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |

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

# **parent**
> str parent(type_id)

Find the owner(s) of the resource.

Get the parent type identifier of the data structure referenced by the identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str

# Find the owner(s) of the resource.
result = LAMP.Type.parent(type_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
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

# **set_attachment**
> bool, date, datetime, dict, float, int, list, str set_attachment(type_id, target, attachment_key, body)



### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str
target = 'target_example' # str
attachment_key = 'attachment_key_example' # str
body = None # bool, date, datetime, dict, float, int, list, str

result = LAMP.Type.set_attachment(type_id, target, attachment_key, body)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **target** | **str**|  |
 **attachment_key** | **str**|  |
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

# **set_dynamic_attachment**
> bool, date, datetime, dict, float, int, list, str set_dynamic_attachment(type_id, target, attachment_key, invoke_once, dynamic_attachment)



### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

type_id = 'type_id_example' # str
target = 'target_example' # str
attachment_key = 'attachment_key_example' # str
invoke_once = True # bool
dynamic_attachment = LAMP.DynamicAttachment() # DynamicAttachment 

result = LAMP.Type.set_dynamic_attachment(type_id, target, attachment_key, invoke_once, dynamic_attachment)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **target** | **str**|  |
 **attachment_key** | **str**|  |
 **invoke_once** | **bool**|  |
 **dynamic_attachment** | [**DynamicAttachment**](DynamicAttachment.md)|  |

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

