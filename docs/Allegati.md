# Allegati


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nome_attachment** | **str** |  | [optional] 
**algoritmo_compressione** | **str** |  | [optional] 
**formato_attachment** | **str** |  | [optional] 
**descrizione_attachment** | **str** |  | [optional] 
**attachment** | **bytearray** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.allegati import Allegati

# TODO update the JSON string below
json = "{}"
# create an instance of Allegati from a JSON string
allegati_instance = Allegati.from_json(json)
# print the JSON string representation of the object
print(Allegati.to_json())

# convert the object into a dict
allegati_dict = allegati_instance.to_dict()
# create an instance of Allegati from a dict
allegati_from_dict = Allegati.from_dict(allegati_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


