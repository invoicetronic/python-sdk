# DatiContratto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**riferimento_numero_linea** | **List[int]** |  | [optional] 
**id_documento** | **str** |  | [optional] 
**data** | **datetime** |  | [optional] 
**num_item** | **str** |  | [optional] 
**codice_commessa_convenzione** | **str** |  | [optional] 
**codice_cup** | **str** |  | [optional] 
**codice_cig** | **str** |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.dati_contratto import DatiContratto

# TODO update the JSON string below
json = "{}"
# create an instance of DatiContratto from a JSON string
dati_contratto_instance = DatiContratto.from_json(json)
# print the JSON string representation of the object
print(DatiContratto.to_json())

# convert the object into a dict
dati_contratto_dict = dati_contratto_instance.to_dict()
# create an instance of DatiContratto from a dict
dati_contratto_from_dict = DatiContratto.from_dict(dati_contratto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


