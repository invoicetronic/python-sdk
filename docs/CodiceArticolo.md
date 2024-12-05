# CodiceArticolo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_tipo** | **str** |  | [optional] 
**codice_valore** | **str** |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.codice_articolo import CodiceArticolo

# TODO update the JSON string below
json = "{}"
# create an instance of CodiceArticolo from a JSON string
codice_articolo_instance = CodiceArticolo.from_json(json)
# print the JSON string representation of the object
print(CodiceArticolo.to_json())

# convert the object into a dict
codice_articolo_dict = codice_articolo_instance.to_dict()
# create an instance of CodiceArticolo from a dict
codice_articolo_from_dict = CodiceArticolo.from_dict(codice_articolo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


