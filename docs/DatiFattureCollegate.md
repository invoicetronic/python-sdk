# DatiFattureCollegate


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
from invoicetronic_sdk.models.dati_fatture_collegate import DatiFattureCollegate

# TODO update the JSON string below
json = "{}"
# create an instance of DatiFattureCollegate from a JSON string
dati_fatture_collegate_instance = DatiFattureCollegate.from_json(json)
# print the JSON string representation of the object
print(DatiFattureCollegate.to_json())

# convert the object into a dict
dati_fatture_collegate_dict = dati_fatture_collegate_instance.to_dict()
# create an instance of DatiFattureCollegate from a dict
dati_fatture_collegate_from_dict = DatiFattureCollegate.from_dict(dati_fatture_collegate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


