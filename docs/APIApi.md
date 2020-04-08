# LAMP.API


Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](APIApi.md#query) | **POST** / | Query the LAMP Database.
[**schema**](APIApi.md#schema) | **GET** / | View the API schema document.


# **query**
> bool, date, datetime, dict, float, int, list, str query(body)

Query the LAMP Database.

Query the LAMP Database using a transformation document. All GET operations in this API schema document are available by replacing the period with an underscore (i.e. `$Participant_view(...)` instead of `Participant.view(...)`). The `origin`, `from`, and `to` parameters of EventStream functions are preserved but the `transform` parameter is not.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

body = 'body_example' # str

    # Query the LAMP Database.
    result = LAMP.API.query(body)
    pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str**

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**0** | 400 Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema**
> bool, date, datetime, dict, float, int, list, str schema()

View the API schema document.

View this API schema document from a live server instance.

### Example

```python
import LAMP
from pprint import pprint

# Enter a context with an instance of the API client
with LAMP.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = LAMP.APIApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # View the API schema document.
        result = LAMP.API.schema()
        pprint(result)
    except LAMP.ApiException as e:
        print("Exception when calling APIApi->schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

