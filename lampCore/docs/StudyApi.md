# LAMP.StudyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_researcher**](StudyApi.md#all_by_researcher) | **GET** /researcher/{id}/study | List all Studies for a Researcher.
[**clone**](StudyApi.md#clone) | **POST** /researcher/{ResearcherId}/study/clone | Create a deep copy of a study. Including activities and sensors
[**create**](StudyApi.md#create) | **POST** /researcher/{id}/study | Create a Study for a Researcher.
[**delete**](StudyApi.md#delete) | **DELETE** /study/{id} | Delete a Study.
[**update**](StudyApi.md#update) | **PUT** /study/{id} | Update a Study.
[**view**](StudyApi.md#view) | **GET** /study/{id} | View a Study.


# **all_by_researcher**
> InlineResponse2006 all_by_researcher(id)

List all Studies for a Researcher.

List all studies for a Researcher.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # List all Studies for a Researcher.
    api_response = api_client.all_by_researcher(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->all_by_researcher: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all Studies for a Researcher.
    api_response = api_client.all_by_researcher(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->all_by_researcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

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

# **clone**
> InlineResponse2009 clone(researcher_id, inline_object)

Create a deep copy of a study. Including activities and sensors

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

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

[**InlineResponse2009**](InlineResponse2009.md)

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

# **create**
> InlineResponse2007 create(id, study)

Create a Study for a Researcher.

Create a Study for a Researcher.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

id = "id_example" # str | 
study = Study(
        name="Psychosis Study",
    ) # Study | 

# example passing only required values which don't have defaults set
try:
    # Create a Study for a Researcher.
    api_response = api_client.create(id, study)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **study** | [**Study**](Study.md)|  |

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

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

# **delete**
> InlineResponse2002 delete(id)

Delete a Study.

Delete a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

id = "id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Delete a Study.
    api_response = api_client.delete(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **update**
> InlineResponse2002 update(id, study)

Update a Study.

Update a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

id = "id_example" # str | 
study = Study(
        name="Psychosis Study",
    ) # Study | 

# example passing only required values which don't have defaults set
try:
    # Update a Study.
    api_response = api_client.update(id, study)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **study** | [**Study**](Study.md)|  |

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

# **view**
> InlineResponse2008 view(id)

View a Study.

View a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Study

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # View a Study.
    api_response = api_client.view(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # View a Study.
    api_response = api_client.view(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling StudyApi->view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

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

