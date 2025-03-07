# DatiOrdineAcquisto


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
from invoicetronic_sdk.models.dati_ordine_acquisto import DatiOrdineAcquisto

# TODO update the JSON string below
json = "{}"
# create an instance of DatiOrdineAcquisto from a JSON string
dati_ordine_acquisto_instance = DatiOrdineAcquisto.from_json(json)
# print the JSON string representation of the object
print(DatiOrdineAcquisto.to_json())

# convert the object into a dict
dati_ordine_acquisto_dict = dati_ordine_acquisto_instance.to_dict()
# create an instance of DatiOrdineAcquisto from a dict
dati_ordine_acquisto_from_dict = DatiOrdineAcquisto.from_dict(dati_ordine_acquisto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


