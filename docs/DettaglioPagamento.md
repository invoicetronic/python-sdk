# DettaglioPagamento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beneficiario** | **str** |  | [optional] 
**modalita_pagamento** | **str** |  | [optional] 
**data_riferimento_termini_pagamento** | **datetime** |  | [optional] 
**giorni_termini_pagamento** | **int** |  | [optional] 
**data_scadenza_pagamento** | **datetime** |  | [optional] 
**importo_pagamento** | **float** |  | [optional] 
**cod_ufficio_postale** | **str** |  | [optional] 
**cognome_quietanzante** | **str** |  | [optional] 
**nome_quietanzante** | **str** |  | [optional] 
**cf_quietanzante** | **str** |  | [optional] 
**titolo_quietanzante** | **str** |  | [optional] 
**istituto_finanziario** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**abi** | **str** |  | [optional] 
**cab** | **str** |  | [optional] 
**bic** | **str** |  | [optional] 
**sconto_pagamento_anticipato** | **float** |  | [optional] 
**data_limite_pagamento_anticipato** | **datetime** |  | [optional] 
**penalita_pagamenti_ritardati** | **float** |  | [optional] 
**data_decorrenza_penale** | **datetime** |  | [optional] 
**codice_pagamento** | **str** |  | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.dettaglio_pagamento import DettaglioPagamento

# TODO update the JSON string below
json = "{}"
# create an instance of DettaglioPagamento from a JSON string
dettaglio_pagamento_instance = DettaglioPagamento.from_json(json)
# print the JSON string representation of the object
print(DettaglioPagamento.to_json())

# convert the object into a dict
dettaglio_pagamento_dict = dettaglio_pagamento_instance.to_dict()
# create an instance of DettaglioPagamento from a dict
dettaglio_pagamento_from_dict = DettaglioPagamento.from_dict(dettaglio_pagamento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


