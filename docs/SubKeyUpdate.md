# SubKeyUpdate

A restricted key to update. All the editable fields are replaced: an omitted `permissions`, `company_ids` or `cors_origins` means none.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Human-readable label, e.g. the name of the tenant the key is for. | 
**active** | **bool** | Whether the key can authenticate. Defaults to true. | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**company_ids** | **List[int]** | Companies the key can access. When omitted or empty, the key can access all the companies of the account, including the ones created later. | [optional] 
**cors_origins** | **List[str]** | Browser origins allowed to call the API with this key (CORS), e.g. &#x60;https://app.example.com&#x60; or &#x60;*.example.com&#x60;. A key used from a browser is public: keep its permissions and companies minimal. | [optional] 
**id** | **int** | Id of the restricted key to update. | [optional] 
**version** | **int** | Row version read with the key, for optimistic concurrency: a stale version fails with 422. | [optional] 

## Example

```python
from invoicetronic_sdk.models.sub_key_update import SubKeyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SubKeyUpdate from a JSON string
sub_key_update_instance = SubKeyUpdate.from_json(json)
# print the JSON string representation of the object
print(SubKeyUpdate.to_json())

# convert the object into a dict
sub_key_update_dict = sub_key_update_instance.to_dict()
# create an instance of SubKeyUpdate from a dict
sub_key_update_from_dict = SubKeyUpdate.from_dict(sub_key_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


