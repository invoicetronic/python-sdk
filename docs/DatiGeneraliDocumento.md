# DatiGeneraliDocumento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_documento** | **str** |  | [optional] 
**divisa** | **str** |  | [optional] 
**data** | **datetime** |  | [optional] 
**numero** | **str** |  | [optional] 
**dati_ritenuta** | [**List[DatiRitenuta]**](DatiRitenuta.md) |  | [optional] 
**dati_bollo** | [**DatiBollo**](DatiBollo.md) |  | [optional] 
**dati_cassa_previdenziale** | [**List[DatiCassaPrevidenziale]**](DatiCassaPrevidenziale.md) |  | [optional] 
**sconto_maggiorazione** | [**List[ScontoMaggiorazione]**](ScontoMaggiorazione.md) |  | [optional] 
**importo_totale_documento** | **float** |  | [optional] 
**arrotondamento** | **float** |  | [optional] 
**causale** | **List[str]** |  | [optional] 
**art73** | **str** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.dati_generali_documento import DatiGeneraliDocumento

# TODO update the JSON string below
json = "{}"
# create an instance of DatiGeneraliDocumento from a JSON string
dati_generali_documento_instance = DatiGeneraliDocumento.from_json(json)
# print the JSON string representation of the object
print(DatiGeneraliDocumento.to_json())

# convert the object into a dict
dati_generali_documento_dict = dati_generali_documento_instance.to_dict()
# create an instance of DatiGeneraliDocumento from a dict
dati_generali_documento_from_dict = DatiGeneraliDocumento.from_dict(dati_generali_documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


