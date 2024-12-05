# AltriDatiGestionali


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_dato** | **str** |  | [optional] 
**riferimento_testo** | **str** |  | [optional] 
**riferimento_numero** | **float** |  | [optional] 
**riferimento_data** | **datetime** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.altri_dati_gestionali import AltriDatiGestionali

# TODO update the JSON string below
json = "{}"
# create an instance of AltriDatiGestionali from a JSON string
altri_dati_gestionali_instance = AltriDatiGestionali.from_json(json)
# print the JSON string representation of the object
print(AltriDatiGestionali.to_json())

# convert the object into a dict
altri_dati_gestionali_dict = altri_dati_gestionali_instance.to_dict()
# create an instance of AltriDatiGestionali from a dict
altri_dati_gestionali_from_dict = AltriDatiGestionali.from_dict(altri_dati_gestionali_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


