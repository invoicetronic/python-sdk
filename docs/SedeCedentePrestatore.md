# SedeCedentePrestatore


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
from invoicetronic_einvoice_sdk.models.sede_cedente_prestatore import SedeCedentePrestatore

# TODO update the JSON string below
json = "{}"
# create an instance of SedeCedentePrestatore from a JSON string
sede_cedente_prestatore_instance = SedeCedentePrestatore.from_json(json)
# print the JSON string representation of the object
print(SedeCedentePrestatore.to_json())

# convert the object into a dict
sede_cedente_prestatore_dict = sede_cedente_prestatore_instance.to_dict()
# create an instance of SedeCedentePrestatore from a dict
sede_cedente_prestatore_from_dict = SedeCedentePrestatore.from_dict(sede_cedente_prestatore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


