# FatturaPrincipale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fattura_principale** | **str** |  | [optional] 
**data_fattura_principale** | **datetime** |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.fattura_principale import FatturaPrincipale

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaPrincipale from a JSON string
fattura_principale_instance = FatturaPrincipale.from_json(json)
# print the JSON string representation of the object
print(FatturaPrincipale.to_json())

# convert the object into a dict
fattura_principale_dict = fattura_principale_instance.to_dict()
# create an instance of FatturaPrincipale from a dict
fattura_principale_from_dict = FatturaPrincipale.from_dict(fattura_principale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


