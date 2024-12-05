# DatiAnagraficiVettore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_fiscale_iva** | [**IdFiscaleIVA**](IdFiscaleIVA.md) |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**numero_licenza_guida** | **str** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.dati_anagrafici_vettore import DatiAnagraficiVettore

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAnagraficiVettore from a JSON string
dati_anagrafici_vettore_instance = DatiAnagraficiVettore.from_json(json)
# print the JSON string representation of the object
print(DatiAnagraficiVettore.to_json())

# convert the object into a dict
dati_anagrafici_vettore_dict = dati_anagrafici_vettore_instance.to_dict()
# create an instance of DatiAnagraficiVettore from a dict
dati_anagrafici_vettore_from_dict = DatiAnagraficiVettore.from_dict(dati_anagrafici_vettore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


