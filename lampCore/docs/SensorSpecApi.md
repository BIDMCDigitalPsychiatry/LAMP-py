# LAMP.SensorSpecApi

All URIs are relative to *https://api.lamp.digital*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](SensorSpecApi.md#all) | **GET** /sensor_spec | List all SensorSpecs.
[**create**](SensorSpecApi.md#create) | **POST** /sensor_spec | Create a SensorSpec.
[**delete**](SensorSpecApi.md#delete) | **DELETE** /sensor_spec/{id} | Delete a SensorSpec.
[**update**](SensorSpecApi.md#update) | **PUT** /sensor_spec/{id} | Update a SensorSpec.
[**view**](SensorSpecApi.md#view) | **GET** /sensor_spec/{id} | View a SensorSpec.


# **all**
> InlineResponse2003 all()

List all SensorSpecs.

List all SensorSpecs.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.SensorSpec

transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all SensorSpecs.
    api_response = api_client.all(transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorSpecApi->all: %s\n" % e)
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
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> InlineResponse2002 create(sensor_spec)

Create a SensorSpec.

Create a SensorSpec.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.SensorSpec

sensor_spec = SensorSpec(
        id="id_example",
        settings_schema=None,
        data_schema=None,
    ) # SensorSpec | 

# example passing only required values which don't have defaults set
try:
    # Create a SensorSpec.
    api_response = api_client.create(sensor_spec)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorSpecApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_spec** | [**SensorSpec**](SensorSpec.md)|  |

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

Delete a SensorSpec.

Delete a SensorSpec.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.SensorSpec

id = "id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Delete a SensorSpec.
    api_response = api_client.delete(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorSpecApi->delete: %s\n" % e)
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
> InlineResponse2002 update(id, sensor_spec)

Update a SensorSpec.

Update a SensorSpec.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.SensorSpec

id = "id_example" # str | 
sensor_spec = SensorSpec(
        id="id_example",
        settings_schema=None,
        data_schema=None,
    ) # SensorSpec | 

# example passing only required values which don't have defaults set
try:
    # Update a SensorSpec.
    api_response = api_client.update(id, sensor_spec)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorSpecApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **sensor_spec** | [**SensorSpec**](SensorSpec.md)|  |

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

View a SensorSpec.

View a SensorSpec.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.SensorSpec

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # View a SensorSpec.
    api_response = api_client.view(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorSpecApi->view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # View a SensorSpec.
    api_response = api_client.view(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorSpecApi->view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

