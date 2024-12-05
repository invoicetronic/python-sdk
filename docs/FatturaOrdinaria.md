# FatturaOrdinaria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sistema_emittente** | **str** |  | [optional] 
**fattura_elettronica_header** | [**FatturaElettronicaHeader**](FatturaElettronicaHeader.md) |  | [optional] 
**fattura_elettronica_body** | [**List[FatturaElettronicaBody]**](FatturaElettronicaBody.md) |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.fattura_ordinaria import FatturaOrdinaria

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaOrdinaria from a JSON string
fattura_ordinaria_instance = FatturaOrdinaria.from_json(json)
# print the JSON string representation of the object
print(FatturaOrdinaria.to_json())

# convert the object into a dict
fattura_ordinaria_dict = fattura_ordinaria_instance.to_dict()
# create an instance of FatturaOrdinaria from a dict
fattura_ordinaria_from_dict = FatturaOrdinaria.from_dict(fattura_ordinaria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


