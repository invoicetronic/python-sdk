# DatiDDT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_ddt** | **str** |  | [optional] 
**data_ddt** | **datetime** |  | [optional] 
**riferimento_numero_linea** | **List[int]** |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.dati_ddt import DatiDDT

# TODO update the JSON string below
json = "{}"
# create an instance of DatiDDT from a JSON string
dati_ddt_instance = DatiDDT.from_json(json)
# print the JSON string representation of the object
print(DatiDDT.to_json())

# convert the object into a dict
dati_ddt_dict = dati_ddt_instance.to_dict()
# create an instance of DatiDDT from a dict
dati_ddt_from_dict = DatiDDT.from_dict(dati_ddt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


