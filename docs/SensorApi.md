# LAMP.Sensor


Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](SensorApi.md#all) | **GET** /sensor | Get the set of all sensors.
[**all_by_participant**](SensorApi.md#all_by_participant) | **GET** /participant/{participant_id}/sensor | Get all sensors for a participant.
[**all_by_researcher**](SensorApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/sensor | Get all sensors for a researcher.
[**all_by_study**](SensorApi.md#all_by_study) | **GET** /study/{study_id}/sensor | View all sensors in a study.
[**create**](SensorApi.md#create) | **POST** /study/{study_id}/sensor | Create a new Sensor under the given Study.
[**delete**](SensorApi.md#delete) | **DELETE** /sensor/{sensor_id} | Delete a Sensor.
[**update**](SensorApi.md#update) | **PUT** /sensor/{sensor_id} | Update an Sensor&#39;s settings.
[**view**](SensorApi.md#view) | **GET** /sensor/{sensor_id} | Get a single sensor, by identifier.


# **all**
> [object] all()

Get the set of all sensors.

Get the set of all sensors.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

# Get the set of all sensors.
result = LAMP.Sensor.all()
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform** | **str**|  | [optional]

### Return type

**[object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_by_participant**
> [object] all_by_participant(participant_id)

Get all sensors for a participant.

Get the set of all sensors available to a participant, by participant  identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

participant_id = 'participant_id_example' # str

# Get all sensors for a participant.
result = LAMP.Sensor.all_by_participant(participant_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

**[object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_by_researcher**
> [object] all_by_researcher(researcher_id)

Get all sensors for a researcher.

Get the set of all sensors available to participants of any study conducted  by a researcher, by researcher identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

researcher_id = 'researcher_id_example' # str

# Get all sensors for a researcher.
result = LAMP.Sensor.all_by_researcher(researcher_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **researcher_id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

**[object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_by_study**
> [object] all_by_study(study_id)

View all sensors in a study.

Get the set of all sensors available to participants of a single  study, by study identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str

# View all sensors in a study.
result = LAMP.Sensor.all_by_study(study_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

**[object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> str create(study_id, sensor)

Create a new Sensor under the given Study.

Create a new Sensor under the given Study.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

study_id = 'study_id_example' # str
sensor = LAMP.Sensor() # Sensor

# Create a new Sensor under the given Study.
result = LAMP.Sensor.create(study_id, sensor)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  |
 **sensor** | [**Sensor**](Sensor.md)|  |

### Return type

**str**

### HTTP request headers

 - **Content-Type**: `application/json`
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> str delete(sensor_id)

Delete a Sensor.

Delete a Sensor.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

sensor_id = 'sensor_id_example' # str

# Delete a Sensor.
result = LAMP.Sensor.delete(sensor_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**|  |

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> str update(sensor_id, sensor)

Update an Sensor's settings.

Update an Sensor's settings.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

sensor_id = 'sensor_id_example' # str
sensor = LAMP.Sensor() # Sensor

# Update an Sensor's settings.
result = LAMP.Sensor.update(sensor_id, sensor)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**|  |
 **sensor** | [**Sensor**](Sensor.md)|  |

### Return type

**str**

### HTTP request headers

 - **Content-Type**: `application/json`
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view**
> [object] view(sensor_id)

Get a single sensor, by identifier.

Get a single sensor, by identifier.

### Example

* Api Key Authentication (Authorization):
```python
import LAMP
from pprint import pprint

sensor_id = 'sensor_id_example' # str

# Get a single sensor, by identifier.
result = LAMP.Sensor.view(sensor_id)
pprint(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**|  |
 **transform** | **str**|  | [optional]

### Return type

**[object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: `application/json`

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Success |  -  |
**400** | 400 Bad Request |  -  |
**403** | 403 Authorization Failed |  -  |
**404** | 404 Not Found |  -  |
**0** | 500 Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

