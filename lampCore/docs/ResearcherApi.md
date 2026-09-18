# LAMP.ResearcherApi

All URIs are relative to *https://api.lamp.digital*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](ResearcherApi.md#all) | **GET** /researcher | List all Researchers.
[**create**](ResearcherApi.md#create) | **POST** /researcher | Create a Researcher.
[**delete**](ResearcherApi.md#delete) | **DELETE** /researcher/{id} | Delete a Researcher.
[**update**](ResearcherApi.md#update) | **PUT** /researcher/{id} | Update a Researcher.
[**view**](ResearcherApi.md#view) | **GET** /researcher/{id} | View a Researcher.


# **all**
> InlineResponse2003 all()

List all Researchers.

This action requires system administrator privileges.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Researcher

transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all Researchers.
    api_response = api_client.all(transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ResearcherApi->all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [OldServer](../README.md#OldServer), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content Available |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> InlineResponse2004 create(request_body)

Create a Researcher.

This action requires system administrator privileges.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Researcher

request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

# example passing only required values which don't have defaults set
try:
    # Create a Researcher.
    api_response = api_client.create(request_body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ResearcherApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **delete**
> InlineResponse2002 delete(id)

Delete a Researcher.

Delete a Researcher.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Researcher

id = "id_example" # str | Researcher Id

# example passing only required values which don't have defaults set
try:
    # Delete a Researcher.
    api_response = api_client.delete(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ResearcherApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Researcher Id |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **update**
> InlineResponse2002 update(id, request_body)

Update a Researcher.

Update a Researcher's settings.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Researcher

id = "id_example" # str | Researcher Id
request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

# example passing only required values which don't have defaults set
try:
    # Update a Researcher.
    api_response = api_client.update(id, request_body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ResearcherApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Researcher Id |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **view**
> InlineResponse2003 view(id)

View a Researcher.

View a Researcher.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Researcher

id = "id_example" # str | Researcher Id
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # View a Researcher.
    api_response = api_client.view(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ResearcherApi->view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # View a Researcher.
    api_response = api_client.view(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ResearcherApi->view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Researcher Id |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

