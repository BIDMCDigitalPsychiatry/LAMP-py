# Credential

Every object can have one or more credential(s) associated with it. (i.e. `my_researcher.credentials = ['person A', 'person B', 'api A'', 'person C', 'api B']`)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** | The root object this credential is attached to. The scope of this credential is limited to the object itself and any children. | [optional] 
**access_key** | **str** | Username or machine-readable public key (access). | [optional] 
**secret_key** | **str** | SALTED HASH OF Password or machine-readable private key (secret). | [optional] 
**description** | **str** | The user-visible description of the credential. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


