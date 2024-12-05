# DatiVeicoli


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **datetime** |  | [optional] 
**totale_percorso** | **str** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.dati_veicoli import DatiVeicoli

# TODO update the JSON string below
json = "{}"
# create an instance of DatiVeicoli from a JSON string
dati_veicoli_instance = DatiVeicoli.from_json(json)
# print the JSON string representation of the object
print(DatiVeicoli.to_json())

# convert the object into a dict
dati_veicoli_dict = dati_veicoli_instance.to_dict()
# create an instance of DatiVeicoli from a dict
dati_veicoli_from_dict = DatiVeicoli.from_dict(dati_veicoli_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


