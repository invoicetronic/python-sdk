# DatiRicezione


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
from invoicetronic_sdk.models.dati_ricezione import DatiRicezione

# TODO update the JSON string below
json = "{}"
# create an instance of DatiRicezione from a JSON string
dati_ricezione_instance = DatiRicezione.from_json(json)
# print the JSON string representation of the object
print(DatiRicezione.to_json())

# convert the object into a dict
dati_ricezione_dict = dati_ricezione_instance.to_dict()
# create an instance of DatiRicezione from a dict
dati_ricezione_from_dict = DatiRicezione.from_dict(dati_ricezione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


