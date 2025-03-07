# DatiBollo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bollo_virtuale** | **str** |  | [optional] 
**importo_bollo** | **float** |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.dati_bollo import DatiBollo

# TODO update the JSON string below
json = "{}"
# create an instance of DatiBollo from a JSON string
dati_bollo_instance = DatiBollo.from_json(json)
# print the JSON string representation of the object
print(DatiBollo.to_json())

# convert the object into a dict
dati_bollo_dict = dati_bollo_instance.to_dict()
# create an instance of DatiBollo from a dict
dati_bollo_from_dict = DatiBollo.from_dict(dati_bollo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


