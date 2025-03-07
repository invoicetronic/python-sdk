# FatturaElettronicaBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dati_generali** | [**DatiGenerali**](DatiGenerali.md) |  | [optional] 
**dati_beni_servizi** | [**DatiBeniServizi**](DatiBeniServizi.md) |  | [optional] 
**dati_veicoli** | [**DatiVeicoli**](DatiVeicoli.md) |  | [optional] 
**dati_pagamento** | [**List[DatiPagamento]**](DatiPagamento.md) |  | [optional] 
**allegati** | [**List[Allegati]**](Allegati.md) |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.fattura_elettronica_body import FatturaElettronicaBody

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaBody from a JSON string
fattura_elettronica_body_instance = FatturaElettronicaBody.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaBody.to_json())

# convert the object into a dict
fattura_elettronica_body_dict = fattura_elettronica_body_instance.to_dict()
# create an instance of FatturaElettronicaBody from a dict
fattura_elettronica_body_from_dict = FatturaElettronicaBody.from_dict(fattura_elettronica_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


