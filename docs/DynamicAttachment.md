# DynamicAttachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key. | [optional] 
**_from** | **str** | A globally unique reference for objects. | [optional] 
**to** | **str** | Either \&quot;me\&quot; to apply to the attachment owner only, the ID of an object owned  by the attachment owner, or a string representing the child object type to apply to. | [optional] 
**triggers** | **[object]** | The API triggers that activate script execution. These will be event stream types  or object types in the API, or, if scheduling execution periodically, a cron-job string  prefixed with \&quot;!\&quot; (exclamation point). | [optional] 
**language** | **str** | The script language. | [optional] 
**contents** | **str** | The script contents. | [optional] 
**requirements** | **[object]** | The script requirements. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


