# SubKeyRequest

A restricted key to create.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Human-readable label, e.g. the name of the tenant the key is for. | 
**active** | **bool** | Whether the key can authenticate. Defaults to true. | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**company_ids** | **List[int]** | Companies the key can access. When omitted or empty, the key can access all the companies of the account, including the ones created later. | [optional] 
**cors_origins** | **List[str]** | Browser origins allowed to call the API with this key (CORS), e.g. &#x60;https://app.example.com&#x60; or &#x60;*.example.com&#x60;. A key used from a browser is public: keep its permissions and companies minimal. | [optional] 

## Example

```python
from invoicetronic_sdk.models.sub_key_request import SubKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubKeyRequest from a JSON string
sub_key_request_instance = SubKeyRequest.from_json(json)
# print the JSON string representation of the object
print(SubKeyRequest.to_json())

# convert the object into a dict
sub_key_request_dict = sub_key_request_instance.to_dict()
# create an instance of SubKeyRequest from a dict
sub_key_request_from_dict = SubKeyRequest.from_dict(sub_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


