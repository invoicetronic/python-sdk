# RappresentanteFiscaleCessionarioCommittente


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione** | **str** |  | [optional] 
**nome** | **str** |  | [optional] 
**cognome** | **str** |  | [optional] 
**id_fiscale_iva** | [**IdFiscaleIVA**](IdFiscaleIVA.md) |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.rappresentante_fiscale_cessionario_committente import RappresentanteFiscaleCessionarioCommittente

# TODO update the JSON string below
json = "{}"
# create an instance of RappresentanteFiscaleCessionarioCommittente from a JSON string
rappresentante_fiscale_cessionario_committente_instance = RappresentanteFiscaleCessionarioCommittente.from_json(json)
# print the JSON string representation of the object
print(RappresentanteFiscaleCessionarioCommittente.to_json())

# convert the object into a dict
rappresentante_fiscale_cessionario_committente_dict = rappresentante_fiscale_cessionario_committente_instance.to_dict()
# create an instance of RappresentanteFiscaleCessionarioCommittente from a dict
rappresentante_fiscale_cessionario_committente_from_dict = RappresentanteFiscaleCessionarioCommittente.from_dict(rappresentante_fiscale_cessionario_committente_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


