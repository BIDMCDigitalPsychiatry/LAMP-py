# JSONSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**schema** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional]  if omitted the server will use the default value of False
**examples** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**multiple_of** | **float** |  | [optional] 
**maximum** | **float** |  | [optional] 
**exclusive_maximum** | **float** |  | [optional] 
**minimum** | **float** |  | [optional] 
**exclusive_minimum** | **float** |  | [optional] 
**max_length** | **int** |  | [optional] 
**min_length** | **int** |  | [optional]  if omitted the server will use the default value of 0
**pattern** | **str** |  | [optional] 
**additional_items** | [**JSONSchema**](JSONSchema.md) |  | [optional] 
**items** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**max_items** | **int** |  | [optional] 
**min_items** | **int** |  | [optional]  if omitted the server will use the default value of 0
**unique_items** | **bool** |  | [optional]  if omitted the server will use the default value of False
**contains** | [**JSONSchema**](JSONSchema.md) |  | [optional] 
**max_properties** | **int** |  | [optional] 
**min_properties** | **int** |  | [optional]  if omitted the server will use the default value of 0
**required** | **[str]** |  | [optional]  if omitted the server will use the default value of []
**additional_properties** | [**JSONSchema**](JSONSchema.md) |  | [optional] 
**definitions** | [**{str: (JSONSchema,)}**](JSONSchema.md) |  | [optional]  if omitted the server will use the default value of {}
**properties** | [**{str: (JSONSchema,)}**](JSONSchema.md) |  | [optional]  if omitted the server will use the default value of {}
**pattern_properties** | [**{str: (JSONSchema,)}**](JSONSchema.md) |  | [optional]  if omitted the server will use the default value of {}
**dependencies** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**property_names** | [**JSONSchema**](JSONSchema.md) |  | [optional] 
**enum** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**type** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**format** | **str** |  | [optional] 
**content_media_type** | **str** |  | [optional] 
**content_encoding** | **str** |  | [optional] 
**_if** | [**JSONSchema**](JSONSchema.md) |  | [optional] 
**then** | [**JSONSchema**](JSONSchema.md) |  | [optional] 
**_else** | [**JSONSchema**](JSONSchema.md) |  | [optional] 
**all_of** | [**[JSONSchema]**](JSONSchema.md) |  | [optional] 
**any_of** | [**[JSONSchema]**](JSONSchema.md) |  | [optional] 
**one_of** | [**[JSONSchema]**](JSONSchema.md) |  | [optional] 
**_not** | [**JSONSchema**](JSONSchema.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


