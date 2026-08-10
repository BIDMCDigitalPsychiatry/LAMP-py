# LAMP.ActivitySpecApi

All URIs are relative to *https://api.lamp.digital*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](ActivitySpecApi.md#all) | **GET** /activity_spec | List all ActivitySpecs.
[**create**](ActivitySpecApi.md#create) | **POST** /activity_spec | Create an ActivitySpec.
[**delete**](ActivitySpecApi.md#delete) | **DELETE** /activity_spec/{id} | Delete an ActivitySpec.
[**update**](ActivitySpecApi.md#update) | **PUT** /activity_spec/{id} | Update an ActivitySpec.
[**view**](ActivitySpecApi.md#view) | **GET** /activity_spec/{id} | View an ActivitySpec.


# **all**
> InlineResponse20010 all()

List all ActivitySpecs.

List all ActivitySpecs.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.ActivitySpec

transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all ActivitySpecs.
    api_response = api_client.all(transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivitySpecApi->all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

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

# **create**
> InlineResponse2002 create(activity_spec)

Create an ActivitySpec.

Create an ActivitySpec.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.ActivitySpec

activity_spec = ActivitySpec(
        help_contents="help_contents_example",
        script_contents="script_contents_example",
        static_data=None,
        temporal_slices=None,
        settings=None,
    ) # ActivitySpec | 

# example passing only required values which don't have defaults set
try:
    # Create an ActivitySpec.
    api_response = api_client.create(activity_spec)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivitySpecApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_spec** | [**ActivitySpec**](ActivitySpec.md)|  |

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

# **delete**
> InlineResponse2002 delete(id)

Delete an ActivitySpec.

Delete an ActivitySpec.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.ActivitySpec

id = "id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Delete an ActivitySpec.
    api_response = api_client.delete(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivitySpecApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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
> InlineResponse2002 update(id, activity_spec)

Update an ActivitySpec.

Update an ActivitySpec.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.ActivitySpec

id = "id_example" # str | 
activity_spec = ActivitySpec(
        help_contents="help_contents_example",
        script_contents="script_contents_example",
        static_data=None,
        temporal_slices=None,
        settings=None,
    ) # ActivitySpec | 

# example passing only required values which don't have defaults set
try:
    # Update an ActivitySpec.
    api_response = api_client.update(id, activity_spec)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivitySpecApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **activity_spec** | [**ActivitySpec**](ActivitySpec.md)|  |

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
> InlineResponse20011 view(id)

View an ActivitySpec.

View an ActivitySpec.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.ActivitySpec

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # View an ActivitySpec.
    api_response = api_client.view(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivitySpecApi->view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # View an ActivitySpec.
    api_response = api_client.view(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivitySpecApi->view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transform** | **str**|  | [optional]

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

