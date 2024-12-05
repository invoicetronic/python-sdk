# DatiAnagrafici


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_fiscale_iva** | [**IdFiscaleIVA**](IdFiscaleIVA.md) |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.dati_anagrafici import DatiAnagrafici

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAnagrafici from a JSON string
dati_anagrafici_instance = DatiAnagrafici.from_json(json)
# print the JSON string representation of the object
print(DatiAnagrafici.to_json())

# convert the object into a dict
dati_anagrafici_dict = dati_anagrafici_instance.to_dict()
# create an instance of DatiAnagrafici from a dict
dati_anagrafici_from_dict = DatiAnagrafici.from_dict(dati_anagrafici_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


