# ActivitySpec

The ActivitySpec determines the parameters and properties of an Activity and its corresponding generated ActivityEvents.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the activity spec. | [optional] 
**help_contents** | **str** | Either a binary blob containing a document or video, or a string containing  instructional aid about the Activity. | [optional] 
**script_contents** | **str** | The WebView-compatible script that provides this Activity on mobile or desktop (IFrame) clients. | [optional] 
**static_data_schema** | **bool, date, datetime, dict, float, int, list, str** | The static data definition of an ActivitySpec. | [optional] 
**temporal_event_schema** | **bool, date, datetime, dict, float, int, list, str** | The temporal event data definition of an ActivitySpec. | [optional] 
**settings_schema** | **bool, date, datetime, dict, float, int, list, str** | The Activity settings definition of an ActivitySpec. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


