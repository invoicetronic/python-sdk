# IscrizioneREA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ufficio** | **str** |  | [optional] 
**numero_rea** | **str** |  | [optional] 
**capitale_sociale** | **float** |  | [optional] 
**socio_unico** | **str** |  | [optional] 
**stato_liquidazione** | **str** |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.iscrizione_rea import IscrizioneREA

# TODO update the JSON string below
json = "{}"
# create an instance of IscrizioneREA from a JSON string
iscrizione_rea_instance = IscrizioneREA.from_json(json)
# print the JSON string representation of the object
print(IscrizioneREA.to_json())

# convert the object into a dict
iscrizione_rea_dict = iscrizione_rea_instance.to_dict()
# create an instance of IscrizioneREA from a dict
iscrizione_rea_from_dict = IscrizioneREA.from_dict(iscrizione_rea_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


