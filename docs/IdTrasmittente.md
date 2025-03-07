# IdTrasmittente


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_paese** | **str** |  | [optional] 
**id_codice** | **str** |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.id_trasmittente import IdTrasmittente

# TODO update the JSON string below
json = "{}"
# create an instance of IdTrasmittente from a JSON string
id_trasmittente_instance = IdTrasmittente.from_json(json)
# print the JSON string representation of the object
print(IdTrasmittente.to_json())

# convert the object into a dict
id_trasmittente_dict = id_trasmittente_instance.to_dict()
# create an instance of IdTrasmittente from a dict
id_trasmittente_from_dict = IdTrasmittente.from_dict(id_trasmittente_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


