# LAMP.AuthenticationApi

All URIs are relative to *https://api.lamp.digital*

Method | HTTP request | Description
------------- | ------------- | -------------
[**server_info**](AuthenticationApi.md#server_info) | **GET** /server-info | 
[**session_info**](AuthenticationApi.md#session_info) | **GET** /session-info | 


# **server_info**
> InlineResponse200 server_info()



### Example

* Basic Authentication (OldServer):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Authentication


# example, this endpoint has no required or optional parameters
try:
    api_response = api_client.server_info()
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling AuthenticationApi->server_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[OldServer](../README.md#OldServer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_info**
> CurrentSessionInfo session_info()



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (MobileToken):
* Basic Authentication (OldServer):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect(server_address="https://api.lamp.digital", api_key="apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Authentication


# example, this endpoint has no required or optional parameters
try:
    api_response = api_client.session_info()
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling AuthenticationApi->session_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentSessionInfo**](CurrentSessionInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [MobileToken](../README.md#MobileToken), [OldServer](../README.md#OldServer), [SessionLogin](../README.md#SessionLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the currently active session |  -  |
**403** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

