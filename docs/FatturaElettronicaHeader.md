# FatturaElettronicaHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dati_trasmissione** | [**DatiTrasmissione**](DatiTrasmissione.md) |  | [optional] 
**cedente_prestatore** | [**CedentePrestatore**](CedentePrestatore.md) |  | [optional] 
**rappresentante_fiscale** | [**RappresentanteFiscale**](RappresentanteFiscale.md) |  | [optional] 
**cessionario_committente** | [**CessionarioCommittente**](CessionarioCommittente.md) |  | [optional] 
**terzo_intermediario_o_soggetto_emittente** | [**TerzoIntermediarioOSoggettoEmittente**](TerzoIntermediarioOSoggettoEmittente.md) |  | [optional] 
**soggetto_emittente** | **str** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.fattura_elettronica_header import FatturaElettronicaHeader

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaHeader from a JSON string
fattura_elettronica_header_instance = FatturaElettronicaHeader.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaHeader.to_json())

# convert the object into a dict
fattura_elettronica_header_dict = fattura_elettronica_header_instance.to_dict()
# create an instance of FatturaElettronicaHeader from a dict
fattura_elettronica_header_from_dict = FatturaElettronicaHeader.from_dict(fattura_elettronica_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


