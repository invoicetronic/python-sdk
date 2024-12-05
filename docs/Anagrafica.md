# Anagrafica


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione** | **str** |  | [optional] 
**nome** | **str** |  | [optional] 
**cognome** | **str** |  | [optional] 
**titolo** | **str** |  | [optional] 
**cod_eori** | **str** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.anagrafica import Anagrafica

# TODO update the JSON string below
json = "{}"
# create an instance of Anagrafica from a JSON string
anagrafica_instance = Anagrafica.from_json(json)
# print the JSON string representation of the object
print(Anagrafica.to_json())

# convert the object into a dict
anagrafica_dict = anagrafica_instance.to_dict()
# create an instance of Anagrafica from a dict
anagrafica_from_dict = Anagrafica.from_dict(anagrafica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


