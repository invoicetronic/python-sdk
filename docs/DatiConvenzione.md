# DatiConvenzione


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
from invoicetronic_einvoice_sdk.models.dati_convenzione import DatiConvenzione

# TODO update the JSON string below
json = "{}"
# create an instance of DatiConvenzione from a JSON string
dati_convenzione_instance = DatiConvenzione.from_json(json)
# print the JSON string representation of the object
print(DatiConvenzione.to_json())

# convert the object into a dict
dati_convenzione_dict = dati_convenzione_instance.to_dict()
# create an instance of DatiConvenzione from a dict
dati_convenzione_from_dict = DatiConvenzione.from_dict(dati_convenzione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


