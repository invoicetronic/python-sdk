# CedentePrestatore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dati_anagrafici** | [**DatiAnagraficiCedentePrestatore**](DatiAnagraficiCedentePrestatore.md) |  | [optional] 
**sede** | [**SedeCedentePrestatore**](SedeCedentePrestatore.md) |  | [optional] 
**stabile_organizzazione** | [**StabileOrganizzazione**](StabileOrganizzazione.md) |  | [optional] 
**iscrizione_rea** | [**IscrizioneREA**](IscrizioneREA.md) |  | [optional] 
**contatti** | [**Contatti**](Contatti.md) |  | [optional] 
**riferimento_amministrazione** | **str** |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.cedente_prestatore import CedentePrestatore

# TODO update the JSON string below
json = "{}"
# create an instance of CedentePrestatore from a JSON string
cedente_prestatore_instance = CedentePrestatore.from_json(json)
# print the JSON string representation of the object
print(CedentePrestatore.to_json())

# convert the object into a dict
cedente_prestatore_dict = cedente_prestatore_instance.to_dict()
# create an instance of CedentePrestatore from a dict
cedente_prestatore_from_dict = CedentePrestatore.from_dict(cedente_prestatore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


