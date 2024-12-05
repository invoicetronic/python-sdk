# DatiGenerali


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dati_generali_documento** | [**DatiGeneraliDocumento**](DatiGeneraliDocumento.md) |  | [optional] 
**dati_ordine_acquisto** | [**List[DatiOrdineAcquisto]**](DatiOrdineAcquisto.md) |  | [optional] 
**dati_contratto** | [**List[DatiContratto]**](DatiContratto.md) |  | [optional] 
**dati_convenzione** | [**List[DatiConvenzione]**](DatiConvenzione.md) |  | [optional] 
**dati_ricezione** | [**List[DatiRicezione]**](DatiRicezione.md) |  | [optional] 
**dati_fatture_collegate** | [**List[DatiFattureCollegate]**](DatiFattureCollegate.md) |  | [optional] 
**dati_sal** | [**List[DatiSAL]**](DatiSAL.md) |  | [optional] 
**dati_ddt** | [**List[DatiDDT]**](DatiDDT.md) |  | [optional] 
**dati_trasporto** | [**DatiTrasporto**](DatiTrasporto.md) |  | [optional] 
**fattura_principale** | [**FatturaPrincipale**](FatturaPrincipale.md) |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.dati_generali import DatiGenerali

# TODO update the JSON string below
json = "{}"
# create an instance of DatiGenerali from a JSON string
dati_generali_instance = DatiGenerali.from_json(json)
# print the JSON string representation of the object
print(DatiGenerali.to_json())

# convert the object into a dict
dati_generali_dict = dati_generali_instance.to_dict()
# create an instance of DatiGenerali from a dict
dati_generali_from_dict = DatiGenerali.from_dict(dati_generali_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


