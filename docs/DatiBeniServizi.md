# DatiBeniServizi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dettaglio_linee** | [**List[DettaglioLinee]**](DettaglioLinee.md) |  | [optional] 
**dati_riepilogo** | [**List[DatiRiepilogo]**](DatiRiepilogo.md) |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.dati_beni_servizi import DatiBeniServizi

# TODO update the JSON string below
json = "{}"
# create an instance of DatiBeniServizi from a JSON string
dati_beni_servizi_instance = DatiBeniServizi.from_json(json)
# print the JSON string representation of the object
print(DatiBeniServizi.to_json())

# convert the object into a dict
dati_beni_servizi_dict = dati_beni_servizi_instance.to_dict()
# create an instance of DatiBeniServizi from a dict
dati_beni_servizi_from_dict = DatiBeniServizi.from_dict(dati_beni_servizi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


