# DatiTrasmissione


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_trasmittente** | [**IdTrasmittente**](IdTrasmittente.md) |  | [optional] 
**progressivo_invio** | **str** |  | [optional] 
**formato_trasmissione** | **str** |  | [optional] 
**codice_destinatario** | **str** |  | [optional] 
**contatti_trasmittente** | [**ContattiTrasmittente**](ContattiTrasmittente.md) |  | [optional] 
**pec_destinatario** | **str** |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.dati_trasmissione import DatiTrasmissione

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasmissione from a JSON string
dati_trasmissione_instance = DatiTrasmissione.from_json(json)
# print the JSON string representation of the object
print(DatiTrasmissione.to_json())

# convert the object into a dict
dati_trasmissione_dict = dati_trasmissione_instance.to_dict()
# create an instance of DatiTrasmissione from a dict
dati_trasmissione_from_dict = DatiTrasmissione.from_dict(dati_trasmissione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


