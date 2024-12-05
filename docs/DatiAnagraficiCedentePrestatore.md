# DatiAnagraficiCedentePrestatore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_fiscale_iva** | [**IdFiscaleIVA**](IdFiscaleIVA.md) |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**albo_professionale** | **str** |  | [optional] 
**provincia_albo** | **str** |  | [optional] 
**numero_iscrizione_albo** | **str** |  | [optional] 
**data_iscrizione_albo** | **datetime** |  | [optional] 
**regime_fiscale** | **str** |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.dati_anagrafici_cedente_prestatore import DatiAnagraficiCedentePrestatore

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAnagraficiCedentePrestatore from a JSON string
dati_anagrafici_cedente_prestatore_instance = DatiAnagraficiCedentePrestatore.from_json(json)
# print the JSON string representation of the object
print(DatiAnagraficiCedentePrestatore.to_json())

# convert the object into a dict
dati_anagrafici_cedente_prestatore_dict = dati_anagrafici_cedente_prestatore_instance.to_dict()
# create an instance of DatiAnagraficiCedentePrestatore from a dict
dati_anagrafici_cedente_prestatore_from_dict = DatiAnagraficiCedentePrestatore.from_dict(dati_anagrafici_cedente_prestatore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


