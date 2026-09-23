# ActivitySpec

The ActivitySpec determines the parameters and properties of an Activity and its corresponding generated ActivityEvents.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The name of the activity spec. | [optional] [readonly] 
**help_contents** | **str** | Either a binary blob containing a document or video, or a string containing  instructional aid about the Activity. | [optional] 
**script_contents** | **str** | The WebView-compatible script that provides this Activity on mobile or desktop (IFrame) clients. | [optional] 
**static_data** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**temporal_slices** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**settings** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


