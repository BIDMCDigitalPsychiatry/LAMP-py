# LAMP.SensorEventApi

All URIs are relative to *https://api.lamp.digital*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_participant**](SensorEventApi.md#all_by_participant) | **GET** /participant/{id}/sensor_event | Query SensorEvents for a Participant.
[**all_by_researcher**](SensorEventApi.md#all_by_researcher) | **GET** /researcher/{id}/sensor_event | Query sensor events across for a researcher&#39;s participants
[**create**](SensorEventApi.md#create) | **POST** /participant/{id}/sensor_event | Create a SensorEvent for a Participant.
[**create_for_researcher**](SensorEventApi.md#create_for_researcher) | **POST** /researcher/{id}/sensor_event | Create a SensorEvent for a Researcher.


# **all_by_participant**
> InlineResponse20021 all_by_participant(id)

Query SensorEvents for a Participant.

List SensorEvents produced by a Participant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.SensorEvent

id = "id_example" # str | 
origin = "origin_example" # str |  (optional)
_from = 1 # int |  (optional)
to = 1 # int |  (optional)
limit = -10 # int |  (optional) if omitted the server will use the default value of 1000
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # Query SensorEvents for a Participant.
    api_response = api_client.all_by_participant(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorEventApi->all_by_participant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Query SensorEvents for a Participant.
    api_response = api_client.all_by_participant(id, origin=origin, _from=_from, to=to, limit=limit, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorEventApi->all_by_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **origin** | **str**|  | [optional]
 **_from** | **int**|  | [optional]
 **to** | **int**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 1000
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

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

# **all_by_researcher**
> InlineResponse20021 all_by_researcher(id)

Query sensor events across for a researcher's participants

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.SensorEvent

id = "researcherId" # str | 
origin = "origin_example" # str |  (optional)
_from = 1 # int |  (optional)
to = 1 # int |  (optional)
limit = -10 # int |  (optional) if omitted the server will use the default value of 1000

# example passing only required values which don't have defaults set
try:
    # Query sensor events across for a researcher's participants
    api_response = api_client.all_by_researcher(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorEventApi->all_by_researcher: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Query sensor events across for a researcher's participants
    api_response = api_client.all_by_researcher(id, origin=origin, _from=_from, to=to, limit=limit)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorEventApi->all_by_researcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **origin** | **str**|  | [optional]
 **_from** | **int**|  | [optional]
 **to** | **int**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 1000

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

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
> InlineResponse2002 create(id, request_body)

Create a SensorEvent for a Participant.

Create a SensorEvent for a Participant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.SensorEvent

id = "id_example" # str | 
request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

# example passing only required values which don't have defaults set
try:
    # Create a SensorEvent for a Participant.
    api_response = api_client.create(id, request_body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorEventApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **create_for_researcher**
> InlineResponse2002 create_for_researcher(id, request_body)

Create a SensorEvent for a Researcher.

Create a SensorEvent for a Researcher.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.SensorEvent

id = "id_example" # str | 
request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

# example passing only required values which don't have defaults set
try:
    # Create a SensorEvent for a Researcher.
    api_response = api_client.create_for_researcher(id, request_body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling SensorEventApi->create_for_researcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

