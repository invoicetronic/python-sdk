# DatiTrasporto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dati_anagrafici_vettore** | [**DatiAnagraficiVettore**](DatiAnagraficiVettore.md) |  | [optional] 
**mezzo_trasporto** | **str** |  | [optional] 
**causale_trasporto** | **str** |  | [optional] 
**numero_colli** | **int** |  | [optional] 
**descrizione** | **str** |  | [optional] 
**unita_misura_peso** | **str** |  | [optional] 
**peso_lordo** | **float** |  | [optional] 
**peso_netto** | **float** |  | [optional] 
**data_ora_ritiro** | **datetime** |  | [optional] 
**data_inizio_trasporto** | **datetime** |  | [optional] 
**tipo_resa** | **str** |  | [optional] 
**indirizzo_resa** | [**IndirizzoResa**](IndirizzoResa.md) |  | [optional] 
**data_ora_consegna** | **datetime** |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.dati_trasporto import DatiTrasporto

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasporto from a JSON string
dati_trasporto_instance = DatiTrasporto.from_json(json)
# print the JSON string representation of the object
print(DatiTrasporto.to_json())

# convert the object into a dict
dati_trasporto_dict = dati_trasporto_instance.to_dict()
# create an instance of DatiTrasporto from a dict
dati_trasporto_from_dict = DatiTrasporto.from_dict(dati_trasporto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


