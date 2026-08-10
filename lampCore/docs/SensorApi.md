# LAMP.SensorApi

All URIs are relative to *https://api.lamp.digital*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_participant**](SensorApi.md#all_by_participant) | **GET** /participant/{id}/sensor | List all Sensors in a Study shared by a Participant.
[**all_by_study**](SensorApi.md#all_by_study) | **GET** /study/{id}/sensor | List all Sensors in a Study.
[**create**](SensorApi.md#create) | **POST** /study/{id}/sensor | Create a Sensor for a Study.
[**delete**](SensorApi.md#delete) | **DELETE** /sensor/{id} | Delete a Sensor.
[**update**](SensorApi.md#update) | **PUT** /sensor/{id} | Update a Sensor.
[**view**](SensorApi.md#view) | **GET** /sensor/{id} | View a Sensor.


# **all_by_participant**
> InlineResponse20018 all_by_participant(id)

List all Sensors in a Study shared by a Participant.

List all Sensors available to a Participant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Sensor

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # List all Sensors in a Study shared by a Participant.
    api_response = api_client.all_by_participant(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorApi->all_by_participant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all Sensors in a Study shared by a Participant.
    api_response = api_client.all_by_participant(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorApi->all_by_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

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

# **all_by_study**
> InlineResponse20018 all_by_study(id)

List all Sensors in a Study.

List all Sensors available to Participants of a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Sensor

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # List all Sensors in a Study.
    api_response = api_client.all_by_study(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorApi->all_by_study: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all Sensors in a Study.
    api_response = api_client.all_by_study(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorApi->all_by_study: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

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
> InlineResponse20019 create(id, sensor)

Create a Sensor for a Study.

Create a Sensor for a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Sensor

id = "id_example" # str | 
sensor = Sensor(
        spec="lamp.accelerometer",
        name="Accelerometer",
        settings={},
    ) # Sensor | 

# example passing only required values which don't have defaults set
try:
    # Create a Sensor for a Study.
    api_response = api_client.create(id, sensor)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **sensor** | [**Sensor**](Sensor.md)|  |

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

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

Delete a Sensor.

Delete a Sensor.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Sensor

id = "id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Delete a Sensor.
    api_response = api_client.delete(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorApi->delete: %s\n" % e)
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
> InlineResponse2002 update(id, sensor)

Update a Sensor.

Update a Sensor.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Sensor

id = "id_example" # str | 
sensor = Sensor(
        spec="lamp.accelerometer",
        name="Accelerometer",
        settings={},
    ) # Sensor | 

# example passing only required values which don't have defaults set
try:
    # Update a Sensor.
    api_response = api_client.update(id, sensor)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **sensor** | [**Sensor**](Sensor.md)|  |

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
> InlineResponse20017 view(id)

View a Sensor.

View a Sensor.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Sensor

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # View a Sensor.
    api_response = api_client.view(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorApi->view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # View a Sensor.
    api_response = api_client.view(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorApi->view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

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

