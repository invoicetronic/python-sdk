# IdFiscaleIVA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_paese** | **str** |  | [optional] 
**id_codice** | **str** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.id_fiscale_iva import IdFiscaleIVA

# TODO update the JSON string below
json = "{}"
# create an instance of IdFiscaleIVA from a JSON string
id_fiscale_iva_instance = IdFiscaleIVA.from_json(json)
# print the JSON string representation of the object
print(IdFiscaleIVA.to_json())

# convert the object into a dict
id_fiscale_iva_dict = id_fiscale_iva_instance.to_dict()
# create an instance of IdFiscaleIVA from a dict
id_fiscale_iva_from_dict = IdFiscaleIVA.from_dict(id_fiscale_iva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


