# StabileOrganizzazione


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indirizzo** | **str** |  | [optional] 
**numero_civico** | **str** |  | [optional] 
**cap** | **str** |  | [optional] 
**comune** | **str** |  | [optional] 
**provincia** | **str** |  | [optional] 
**nazione** | **str** |  | [optional] [default to 'IT']

## Example

```python
from invoicetronic_sdk.models.stabile_organizzazione import StabileOrganizzazione

# TODO update the JSON string below
json = "{}"
# create an instance of StabileOrganizzazione from a JSON string
stabile_organizzazione_instance = StabileOrganizzazione.from_json(json)
# print the JSON string representation of the object
print(StabileOrganizzazione.to_json())

# convert the object into a dict
stabile_organizzazione_dict = stabile_organizzazione_instance.to_dict()
# create an instance of StabileOrganizzazione from a dict
stabile_organizzazione_from_dict = StabileOrganizzazione.from_dict(stabile_organizzazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


