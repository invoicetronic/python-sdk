# RappresentanteFiscale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dati_anagrafici** | [**DatiAnagrafici**](DatiAnagrafici.md) |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.rappresentante_fiscale import RappresentanteFiscale

# TODO update the JSON string below
json = "{}"
# create an instance of RappresentanteFiscale from a JSON string
rappresentante_fiscale_instance = RappresentanteFiscale.from_json(json)
# print the JSON string representation of the object
print(RappresentanteFiscale.to_json())

# convert the object into a dict
rappresentante_fiscale_dict = rappresentante_fiscale_instance.to_dict()
# create an instance of RappresentanteFiscale from a dict
rappresentante_fiscale_from_dict = RappresentanteFiscale.from_dict(rappresentante_fiscale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


