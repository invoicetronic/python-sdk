# DatiRiepilogo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliquota_iva** | **float** |  | [optional] 
**natura** | **str** |  | [optional] 
**spese_accessorie** | **float** |  | [optional] 
**arrotondamento** | **float** |  | [optional] 
**imponibile_importo** | **float** |  | [optional] 
**imposta** | **float** |  | [optional] 
**esigibilita_iva** | **str** |  | [optional] 
**riferimento_normativo** | **str** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.dati_riepilogo import DatiRiepilogo

# TODO update the JSON string below
json = "{}"
# create an instance of DatiRiepilogo from a JSON string
dati_riepilogo_instance = DatiRiepilogo.from_json(json)
# print the JSON string representation of the object
print(DatiRiepilogo.to_json())

# convert the object into a dict
dati_riepilogo_dict = dati_riepilogo_instance.to_dict()
# create an instance of DatiRiepilogo from a dict
dati_riepilogo_from_dict = DatiRiepilogo.from_dict(dati_riepilogo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


