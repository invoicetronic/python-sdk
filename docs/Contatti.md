# Contatti


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**telefono** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.contatti import Contatti

# TODO update the JSON string below
json = "{}"
# create an instance of Contatti from a JSON string
contatti_instance = Contatti.from_json(json)
# print the JSON string representation of the object
print(Contatti.to_json())

# convert the object into a dict
contatti_dict = contatti_instance.to_dict()
# create an instance of Contatti from a dict
contatti_from_dict = Contatti.from_dict(contatti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


