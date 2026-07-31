# LAMP.ActivityEventApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_participant**](ActivityEventApi.md#all_by_participant) | **GET** /participant/{id}/activity_event | Query ActivityEvents for a Participant.
[**create**](ActivityEventApi.md#create) | **POST** /participant/{id}/activity_event | Create an ActivityEvent for a Participant.


# **all_by_participant**
> InlineResponse20020 all_by_participant(id)

Query ActivityEvents for a Participant.

List ActivityEvents produced by a Participant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.ActivityEvent

id = "id_example" # str | 
origin = "origin_example" # str |  (optional)
_from = 1 # int |  (optional)
to = 1 # int |  (optional)
limit = -10 # int |  (optional) if omitted the server will use the default value of 1000
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # Query ActivityEvents for a Participant.
    api_response = api_client.all_by_participant(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityEventApi->all_by_participant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Query ActivityEvents for a Participant.
    api_response = api_client.all_by_participant(id, origin=origin, _from=_from, to=to, limit=limit, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityEventApi->all_by_participant: %s\n" % e)
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

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [SessionLogin](../README.md#SessionLogin)

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

Create an ActivityEvent for a Participant.

Create an ActivityEvent for a Participant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.ActivityEvent

id = "id_example" # str | 
request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

# example passing only required values which don't have defaults set
try:
    # Create an ActivityEvent for a Participant.
    api_response = api_client.create(id, request_body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityEventApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

