# ContattiTrasmittente


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**telefono** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.contatti_trasmittente import ContattiTrasmittente

# TODO update the JSON string below
json = "{}"
# create an instance of ContattiTrasmittente from a JSON string
contatti_trasmittente_instance = ContattiTrasmittente.from_json(json)
# print the JSON string representation of the object
print(ContattiTrasmittente.to_json())

# convert the object into a dict
contatti_trasmittente_dict = contatti_trasmittente_instance.to_dict()
# create an instance of ContattiTrasmittente from a dict
contatti_trasmittente_from_dict = ContattiTrasmittente.from_dict(contatti_trasmittente_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


