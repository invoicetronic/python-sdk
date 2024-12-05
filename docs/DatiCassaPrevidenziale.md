# DatiCassaPrevidenziale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_cassa** | **str** |  | [optional] 
**al_cassa** | **float** |  | [optional] 
**importo_contributo_cassa** | **float** |  | [optional] 
**imponibile_cassa** | **float** |  | [optional] 
**aliquota_iva** | **float** |  | [optional] 
**ritenuta** | **str** |  | [optional] 
**natura** | **str** |  | [optional] 
**riferimento_amministrazione** | **str** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.dati_cassa_previdenziale import DatiCassaPrevidenziale

# TODO update the JSON string below
json = "{}"
# create an instance of DatiCassaPrevidenziale from a JSON string
dati_cassa_previdenziale_instance = DatiCassaPrevidenziale.from_json(json)
# print the JSON string representation of the object
print(DatiCassaPrevidenziale.to_json())

# convert the object into a dict
dati_cassa_previdenziale_dict = dati_cassa_previdenziale_instance.to_dict()
# create an instance of DatiCassaPrevidenziale from a dict
dati_cassa_previdenziale_from_dict = DatiCassaPrevidenziale.from_dict(dati_cassa_previdenziale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


