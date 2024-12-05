# IndirizzoResa


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
from invoicetronic_invoice_sdk.models.indirizzo_resa import IndirizzoResa

# TODO update the JSON string below
json = "{}"
# create an instance of IndirizzoResa from a JSON string
indirizzo_resa_instance = IndirizzoResa.from_json(json)
# print the JSON string representation of the object
print(IndirizzoResa.to_json())

# convert the object into a dict
indirizzo_resa_dict = indirizzo_resa_instance.to_dict()
# create an instance of IndirizzoResa from a dict
indirizzo_resa_from_dict = IndirizzoResa.from_dict(indirizzo_resa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


