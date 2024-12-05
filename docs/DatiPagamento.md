# DatiPagamento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condizioni_pagamento** | **str** |  | [optional] 
**dettaglio_pagamento** | [**List[DettaglioPagamento]**](DettaglioPagamento.md) |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.dati_pagamento import DatiPagamento

# TODO update the JSON string below
json = "{}"
# create an instance of DatiPagamento from a JSON string
dati_pagamento_instance = DatiPagamento.from_json(json)
# print the JSON string representation of the object
print(DatiPagamento.to_json())

# convert the object into a dict
dati_pagamento_dict = dati_pagamento_instance.to_dict()
# create an instance of DatiPagamento from a dict
dati_pagamento_from_dict = DatiPagamento.from_dict(dati_pagamento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


