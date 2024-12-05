# DatiAnagraficiCessionarioCommittente


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_fiscale_iva** | [**IdFiscaleIVA**](IdFiscaleIVA.md) |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.dati_anagrafici_cessionario_committente import DatiAnagraficiCessionarioCommittente

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAnagraficiCessionarioCommittente from a JSON string
dati_anagrafici_cessionario_committente_instance = DatiAnagraficiCessionarioCommittente.from_json(json)
# print the JSON string representation of the object
print(DatiAnagraficiCessionarioCommittente.to_json())

# convert the object into a dict
dati_anagrafici_cessionario_committente_dict = dati_anagrafici_cessionario_committente_instance.to_dict()
# create an instance of DatiAnagraficiCessionarioCommittente from a dict
dati_anagrafici_cessionario_committente_from_dict = DatiAnagraficiCessionarioCommittente.from_dict(dati_anagrafici_cessionario_committente_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


