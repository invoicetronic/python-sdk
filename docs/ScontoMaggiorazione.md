# ScontoMaggiorazione


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo** | **str** |  | [optional] 
**percentuale** | **float** |  | [optional] 
**importo** | **float** |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.sconto_maggiorazione import ScontoMaggiorazione

# TODO update the JSON string below
json = "{}"
# create an instance of ScontoMaggiorazione from a JSON string
sconto_maggiorazione_instance = ScontoMaggiorazione.from_json(json)
# print the JSON string representation of the object
print(ScontoMaggiorazione.to_json())

# convert the object into a dict
sconto_maggiorazione_dict = sconto_maggiorazione_instance.to_dict()
# create an instance of ScontoMaggiorazione from a dict
sconto_maggiorazione_from_dict = ScontoMaggiorazione.from_dict(sconto_maggiorazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


