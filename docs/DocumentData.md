# DocumentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.document_data import DocumentData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentData from a JSON string
document_data_instance = DocumentData.from_json(json)
# print the JSON string representation of the object
print(DocumentData.to_json())

# convert the object into a dict
document_data_dict = document_data_instance.to_dict()
# create an instance of DocumentData from a dict
document_data_from_dict = DocumentData.from_dict(document_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


