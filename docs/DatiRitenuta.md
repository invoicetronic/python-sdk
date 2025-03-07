# DatiRitenuta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_ritenuta** | **str** |  | [optional] 
**importo_ritenuta** | **float** |  | [optional] 
**aliquota_ritenuta** | **float** |  | [optional] 
**causale_pagamento** | **str** |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.dati_ritenuta import DatiRitenuta

# TODO update the JSON string below
json = "{}"
# create an instance of DatiRitenuta from a JSON string
dati_ritenuta_instance = DatiRitenuta.from_json(json)
# print the JSON string representation of the object
print(DatiRitenuta.to_json())

# convert the object into a dict
dati_ritenuta_dict = dati_ritenuta_instance.to_dict()
# create an instance of DatiRitenuta from a dict
dati_ritenuta_from_dict = DatiRitenuta.from_dict(dati_ritenuta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


