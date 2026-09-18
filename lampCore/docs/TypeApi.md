# LAMP.TypeApi

All URIs are relative to *https://api.lamp.digital*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attachment**](TypeApi.md#get_attachment) | **GET** /type/{type_id}/attachment/{attachment_key} | Get the value of an attachment
[**get_tag**](TypeApi.md#get_tag) | **GET** /type/{id}/tag/{key} | Get the value of a tag
[**list_attachments**](TypeApi.md#list_attachments) | **GET** /type/{type_id}/attachment | Get a list of attachment names
[**list_tags**](TypeApi.md#list_tags) | **GET** /type/{id}/tag | Get a list of tag names
[**parent**](TypeApi.md#parent) | **GET** /type/{type_id}/parent | Find the Parent of the Object.
[**set_attachment**](TypeApi.md#set_attachment) | **PUT** /type/{type_id}/attachment/{attachment_key}/{target} | Set or delete an attachment
[**set_tag**](TypeApi.md#set_tag) | **PUT** /type/{id}/tag/{key}/{target} | Set or delete a tag


# **get_attachment**
> InlineResponse20012 get_attachment(type_id, attachment_key)

Get the value of an attachment

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Type

type_id = "type_id_example" # str | 
attachment_key = "attachment_key_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Get the value of an attachment
    api_response = api_client.get_attachment(type_id, attachment_key)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling TypeApi->get_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **attachment_key** | **str**|  |

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [OldServer](../README.md#OldServer), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> InlineResponse20012 get_tag(id, key)

Get the value of a tag

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Type

id = "id_example" # str | 
key = "key_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Get the value of a tag
    api_response = api_client.get_tag(id, key)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling TypeApi->get_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **key** | **str**|  |

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [OldServer](../README.md#OldServer), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachments**
> InlineResponse20011 list_attachments(type_id)

Get a list of attachment names

Get a list of attachment names

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Type

type_id = "type_id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Get a list of attachment names
    api_response = api_client.list_attachments(type_id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling TypeApi->list_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [OldServer](../README.md#OldServer), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> InlineResponse20011 list_tags(id)

Get a list of tag names

Get a list of tag names

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Type

id = "id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Get a list of tag names
    api_response = api_client.list_tags(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling TypeApi->list_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [OldServer](../README.md#OldServer), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parent**
> InlineResponse2001 parent(type_id)

Find the Parent of the Object.

Get the parent type identifier of the data structure referenced by the identifier.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Type

type_id = "type_id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # Find the Parent of the Object.
    api_response = api_client.parent(type_id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling TypeApi->parent: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Find the Parent of the Object.
    api_response = api_client.parent(type_id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling TypeApi->parent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [OldServer](../README.md#OldServer), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_attachment**
> InlineResponse2001 set_attachment(type_id, target, attachment_key, body)

Set or delete an attachment

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Type

type_id = "type_id_example" # str | 
target = "target_example" # str | 
attachment_key = "attachment_key_example" # str | 
body = None # bool, date, datetime, dict, float, int, list, str, none_type | 

# example passing only required values which don't have defaults set
try:
    # Set or delete an attachment
    api_response = api_client.set_attachment(type_id, target, attachment_key, body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling TypeApi->set_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  |
 **target** | **str**|  |
 **attachment_key** | **str**|  |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [OldServer](../README.md#OldServer), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tag**
> InlineResponse2001 set_tag(id, key, target)

Set or delete a tag

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Type

id = "id_example" # str | 
key = "key_example" # str | 
target = "target_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Set or delete a tag
    api_response = api_client.set_tag(id, key, target)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling TypeApi->set_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **key** | **str**|  |
 **target** | **str**|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [OldServer](../README.md#OldServer), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

