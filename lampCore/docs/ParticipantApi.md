# LAMP.ParticipantApi

All URIs are relative to *https://api.lamp.digital*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_study**](ParticipantApi.md#all_by_study) | **GET** /study/{study_id}/participant | List all Participants for a Study.
[**create**](ParticipantApi.md#create) | **POST** /study/{study_id}/participant | Create a Participant for a Study.
[**delete**](ParticipantApi.md#delete) | **DELETE** /participant/{participant_id} | Delete a Participant.
[**update**](ParticipantApi.md#update) | **PUT** /participant/{participant_id} | Update a Participant.
[**view**](ParticipantApi.md#view) | **GET** /participant/{participant_id} | View a Participant.


# **all_by_study**
> InlineResponse2003 all_by_study(study_id)

List all Participants for a Study.

List all Participants in a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Participant

study_id = "study_id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # List all Participants for a Study.
    api_response = api_client.all_by_study(study_id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ParticipantApi->all_by_study: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all Participants for a Study.
    api_response = api_client.all_by_study(study_id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ParticipantApi->all_by_study: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
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
> InlineResponse2002 create(study_id, participant)

Create a Participant for a Study.

Create a Participant for a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Participant

study_id = "study_id_example" # str | 
participant = Participant(
    ) # Participant | 

# example passing only required values which don't have defaults set
try:
    # Create a Participant for a Study.
    api_response = api_client.create(study_id, participant)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ParticipantApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
 **participant** | [**Participant**](Participant.md)|  |

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
> InlineResponse2002 delete(participant_id)

Delete a Participant.

All owned data or event streams will be permanently deleted.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Participant

participant_id = "participant_id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Delete a Participant.
    api_response = api_client.delete(participant_id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ParticipantApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |

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
> InlineResponse2002 update(participant_id, request_body)

Update a Participant.

Update a Participant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Participant

participant_id = "participant_id_example" # str | 
request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

# example passing only required values which don't have defaults set
try:
    # Update a Participant.
    api_response = api_client.update(participant_id, request_body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ParticipantApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
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
> InlineResponse2001 view(participant_id)

View a Participant.

Get a single participant, by identifier.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Participant

participant_id = "participant_id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # View a Participant.
    api_response = api_client.view(participant_id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ParticipantApi->view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # View a Participant.
    api_response = api_client.view(participant_id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ParticipantApi->view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
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

