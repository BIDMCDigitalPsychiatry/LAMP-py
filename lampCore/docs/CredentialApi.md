# LAMP.CredentialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CredentialApi.md#create) | **POST** /type/{id}/credential | Create a new credential
[**delete**](CredentialApi.md#delete) | **DELETE** /type/{id}/credential/{access_key} | Delete a credential
[**list**](CredentialApi.md#list) | **GET** /type/{id}/credential | List credentials
[**update**](CredentialApi.md#update) | **PUT** /type/{id}/credential/{access_key} | Update a credential


# **create**
> InlineResponse20022 create(id, credential)

Create a new credential

Create a new credential tied to this object

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Credential

id = "id_example" # str | 
credential = Credential(
        id="id_example",
        account_setup_state=AccountSetupState("INCOMPLETE"),
        user_type=UserType("participant"),
        origin="U1234567890",
        access_key="my_email@address.com",
        secret_key="secret_key_example",
        description="Firstname Lastname",
        username="username",
    ) # Credential | 

# example passing only required values which don't have defaults set
try:
    # Create a new credential
    api_response = api_client.create(id, credential)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling CredentialApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **credential** | [**Credential**](Credential.md)|  |

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

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
> InlineResponse20022 delete(id, access_key)

Delete a credential

Delete the credential with the given access key

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Credential

id = "id_example" # str | 
access_key = "email@example.com" # str | 

# example passing only required values which don't have defaults set
try:
    # Delete a credential
    api_response = api_client.delete(id, access_key)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling CredentialApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **access_key** | **str**|  |

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

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

# **list**
> InlineResponse20024 list(id)

List credentials

List credentials tied to this object

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Credential

id = "id_example" # str | 

# example passing only required values which don't have defaults set
try:
    # List credentials
    api_response = api_client.list(id)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling CredentialApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

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
> InlineResponse20022 update(id, access_key, credential)

Update a credential

Update the credential with the given access key

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (SessionLogin):

```python

import LAMP


LAMP.connect("http://localhost", "apiKeyValue")

# Enter a context with an instance of the API client
api_client = LAMP.Credential

id = "id_example" # str | 
access_key = "email@example.com" # str | 
credential = Credential(
        id="id_example",
        account_setup_state=AccountSetupState("INCOMPLETE"),
        user_type=UserType("participant"),
        origin="U1234567890",
        access_key="my_email@address.com",
        secret_key="secret_key_example",
        description="Firstname Lastname",
        username="username",
    ) # Credential | 

# example passing only required values which don't have defaults set
try:
    # Update a credential
    api_response = api_client.update(id, access_key, credential)
    print(api_response)
except LAMP.ApiException as e:
    print("Exception when calling CredentialApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **access_key** | **str**|  |
 **credential** | [**Credential**](Credential.md)|  |

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

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

