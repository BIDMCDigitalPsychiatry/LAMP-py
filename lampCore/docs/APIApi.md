# LAMP.APIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](APIApi.md#query) | **POST** / | Query the LAMP Database.
[**schema**](APIApi.md#schema) | **GET** / | View the API Schema.


# **query**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} query(body)

Query the LAMP Database.

Query the LAMP Database using a transformation document. All GET operations in this API schema document are available by replacing the period with an underscore (i.e. `$Participant_view(...)` instead of `Participant.view(...)`). The `origin`, `from`, and `to` parameters of EventStream functions are preserved but the `transform` parameter is not.

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.API

body = "body_example" # str | 

# example passing only required values which don't have defaults set
try:
    # Query the LAMP Database.
    api_response = api_client.query(body)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling APIApi->query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data Queried |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} schema()

View the API Schema.

View this API schema document from a live server instance.

### Example


```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.API


# example, this endpoint has no required or optional parameters
try:
    # View the API Schema.
    api_response = api_client.schema()
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling APIApi->schema: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content Available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

