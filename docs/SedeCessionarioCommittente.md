# SedeCessionarioCommittente


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
from invoicetronic_sdk.models.sede_cessionario_committente import SedeCessionarioCommittente

# TODO update the JSON string below
json = "{}"
# create an instance of SedeCessionarioCommittente from a JSON string
sede_cessionario_committente_instance = SedeCessionarioCommittente.from_json(json)
# print the JSON string representation of the object
print(SedeCessionarioCommittente.to_json())

# convert the object into a dict
sede_cessionario_committente_dict = sede_cessionario_committente_instance.to_dict()
# create an instance of SedeCessionarioCommittente from a dict
sede_cessionario_committente_from_dict = SedeCessionarioCommittente.from_dict(sede_cessionario_committente_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


