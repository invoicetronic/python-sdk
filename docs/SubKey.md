# SubKey

A restricted key. Its secrets are returned only when the key is created or rolled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. | [optional] 
**created** | **datetime** | Creation date. | [optional] [readonly] 
**version** | **int** | Row version, for optimistic concurrency. | [optional] [readonly] 
**description** | **str** | Human-readable label. | [optional] 
**active** | **bool** | Whether the key can authenticate. | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**company_ids** | **List[int]** | Companies the key can access. Empty means all the companies of the account. | [optional] 
**cors_origins** | **List[str]** | Browser origins allowed to call the API with this key (CORS). | [optional] 
**previous_key_expires_at** | **datetime** | When the secrets replaced by the last roll stop working; null when there are none still valid. | [optional] 

## Example

```python
from invoicetronic_sdk.models.sub_key import SubKey

# TODO update the JSON string below
json = "{}"
# create an instance of SubKey from a JSON string
sub_key_instance = SubKey.from_json(json)
# print the JSON string representation of the object
print(SubKey.to_json())

# convert the object into a dict
sub_key_dict = sub_key_instance.to_dict()
# create an instance of SubKey from a dict
sub_key_from_dict = SubKey.from_dict(sub_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


