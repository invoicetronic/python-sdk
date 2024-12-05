# Receive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. Leave it at 0 for new records as it will be set automatically. | [optional] 
**created** | **datetime** | Creation date. It is set automatically. | [optional] 
**version** | **int** | Row version, for optimistic concurrency. It is set automatically. | [optional] 
**user_id** | **int** | User id. | [optional] 
**company_id** | **int** | Company id. On send, this is the sender and must be set in advance. On receive, it will be  automatically set based on the recipient&#39;s VAT number. If a matching company is not found, the invoice will be rejected until the company is created. | [optional] 
**committente** | **str** | VAT number of the Cessionario/Committente (customer). This is automatically set based on the recipient&#39;s VAT number. | [optional] 
**prestatore** | **str** | VAT number of the Cedente/Prestatore (vendor). This is automatically set based on the sender&#39;s VAT number. | [optional] 
**identifier** | **str** | SDI identifier. This is set by the SDI and is guaranted to be unique within the SDI system. | [optional] 
**file_name** | **str** | Xml file name. | [optional] 
**format** | **str** | SDI format (FPA12, FPR12, FSM10, ...) | [optional] 
**payload** | **str** | Xml payloaad. This is the actual xml content, as string. On send, it can be base64 encoded. If it&#39;s not, it will be encoded before sending. It is guaranteed to be cyphered at rest. | [optional] 
**last_update** | **datetime** | Last update from SDI. | [optional] 
**date_sent** | **datetime** | When the invoice was sent to SDI. | [optional] 
**documents** | [**List[DocumentData]**](DocumentData.md) | The invoices included in the payload. This is set by the system, based on the xml content. | [optional] 
**is_read** | **bool** | Wether the invoice has been read at least once. | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.receive import Receive

# TODO update the JSON string below
json = "{}"
# create an instance of Receive from a JSON string
receive_instance = Receive.from_json(json)
# print the JSON string representation of the object
print(Receive.to_json())

# convert the object into a dict
receive_dict = receive_instance.to_dict()
# create an instance of Receive from a dict
receive_from_dict = Receive.from_dict(receive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


