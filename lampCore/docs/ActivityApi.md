# LAMP.ActivityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_by_participant**](ActivityApi.md#all_by_participant) | **GET** /participant/{id}/activity | List all Activities in a Study shared by a Participant.
[**all_by_study**](ActivityApi.md#all_by_study) | **GET** /study/{id}/activity | List all Activities for a Study.
[**create**](ActivityApi.md#create) | **POST** /study/{id}/activity | Create an Activity for a Study.
[**delete**](ActivityApi.md#delete) | **DELETE** /activity/{id} | Delete an Activity.
[**update**](ActivityApi.md#update) | **PUT** /activity/{id} | Update an Activity.
[**view**](ActivityApi.md#view) | **GET** /activity/{id} | View an Activity.


# **all_by_participant**
> InlineResponse20015 all_by_participant(id)

List all Activities in a Study shared by a Participant.

List all Activities available to a Participant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Activity

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # List all Activities in a Study shared by a Participant.
    api_response = api_client.all_by_participant(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityApi->all_by_participant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all Activities in a Study shared by a Participant.
    api_response = api_client.all_by_participant(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityApi->all_by_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

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

# **all_by_study**
> InlineResponse20015 all_by_study(id)

List all Activities for a Study.

List all Activities available to Participants of a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Activity

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # List all Activities for a Study.
    api_response = api_client.all_by_study(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityApi->all_by_study: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # List all Activities for a Study.
    api_response = api_client.all_by_study(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityApi->all_by_study: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

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
> InlineResponse20016 create(id, activity)

Create an Activity for a Study.

Create an Activity for a Study.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Activity

id = "id_example" # str | 
activity = Activity(
        spec="lamp.survey",
        name="Mood Survey",
        settings={},
        schedule=[
            None,
        ],
    ) # Activity | 

# example passing only required values which don't have defaults set
try:
    # Create an Activity for a Study.
    api_response = api_client.create(id, activity)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **activity** | [**Activity**](Activity.md)|  |

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

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

Delete an Activity.

Delete an Activity.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Activity

id = "id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Delete an Activity.
    api_response = api_client.delete(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityApi->delete: %s\n" % e)
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
> InlineResponse2002 update(id, activity)

Update an Activity.

Update an Activity.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Activity

id = "id_example" # str | 
activity = Activity(
        spec="lamp.survey",
        name="Mood Survey",
        settings={},
        schedule=[
            None,
        ],
    ) # Activity | 

# example passing only required values which don't have defaults set
try:
    # Update an Activity.
    api_response = api_client.update(id, activity)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **activity** | [**Activity**](Activity.md)|  |

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
> InlineResponse20014 view(id)

View an Activity.

View an Activity.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Activity

id = "id_example" # str | 
transform = "transform_example" # str |  (optional)

# example passing only required values which don't have defaults set
try:
    # View an Activity.
    api_response = api_client.view(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityApi->view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # View an Activity.
    api_response = api_client.view(id, transform=transform)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling ActivityApi->view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

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

