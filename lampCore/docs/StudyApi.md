# LAMP.StudyApi

All URIs are relative to *https://api.lamp.digital*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_researcher**](StudyApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/study | List all Studies for a Researcher.
[**clone**](StudyApi.md#clone) | **POST** /researcher/{ResearcherId}/study/clone | Create a deep copy of a study. Including activities and sensors
[**create**](StudyApi.md#create) | **POST** /researcher/{researcher_id}/study | Create a Study for a Researcher.
[**delete**](StudyApi.md#delete) | **DELETE** /study/{study_id} | Delete a Study.
[**update**](StudyApi.md#update) | **PUT** /study/{study_id} | Update a Study.
[**view**](StudyApi.md#view) | **GET** /study/{study_id} | View a Study.


# **all_by_researcher**
> InlineResponse2003 all_by_researcher(researcher_id)

List all Studies for a Researcher.

List all studies for a Researcher.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

researcher_id = "researcher_id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # List all Studies for a Researcher.
    api_response = api_client.all_by_researcher(researcher_id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->all_by_researcher: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all Studies for a Researcher.
    api_response = api_client.all_by_researcher(researcher_id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->all_by_researcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_id** | **str**|  |
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

# **clone**
> InlineResponse2006 clone(researcher_id, inline_object)

Create a deep copy of a study. Including activities and sensors

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

researcher_id = "ResearcherId_example" # str | 
inline_object = InlineObject(
        study_id="study_id_example",
        name="name_example",
    ) # InlineObject | 

# example passing only required values which don't have defaults set
try:
    # Create a deep copy of a study. Including activities and sensors
    api_response = api_client.clone(researcher_id, inline_object)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->clone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_id** | **str**|  |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

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

# **create**
> InlineResponse2005 create(researcher_id, request_body)

Create a Study for a Researcher.

Create a Study for a Researcher.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

researcher_id = "researcher_id_example" # str | 
request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

# example passing only required values which don't have defaults set
try:
    # Create a Study for a Researcher.
    api_response = api_client.create(researcher_id, request_body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_id** | **str**|  |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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
> InlineResponse2002 delete(study_id)

Delete a Study.

Delete a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

study_id = "study_id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Delete a Study.
    api_response = api_client.delete(study_id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |

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
> InlineResponse2002 update(study_id, request_body)

Update a Study.

Update a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

study_id = "study_id_example" # str | 
request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

# example passing only required values which don't have defaults set
try:
    # Update a Study.
    api_response = api_client.update(study_id, request_body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
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
> InlineResponse2003 view(study_id)

View a Study.

View a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

study_id = "study_id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # View a Study.
    api_response = api_client.view(study_id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # View a Study.
    api_response = api_client.view(study_id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->view: %s\n" % e)
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

