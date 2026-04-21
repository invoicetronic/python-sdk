# Send

A sent invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. For POST requests, leave it at &#x60;0&#x60; — the server will assign one automatically. For PUT requests, set it to the id of the record you want to update. | [optional] 
**created** | **datetime** | Creation date. It is set automatically. | [optional] [readonly] 
**version** | **int** | Row version, for optimistic concurrency. It is set automatically. | [optional] [readonly] 
**user_id** | **int** | User id. It is set automatically based on the authenticated user. | [optional] [readonly] 
**company_id** | **int** | Company id. It is set automatically based on the VAT number extracted from the invoice payload (the sender for &#x60;send&#x60;, the recipient for &#x60;receive&#x60;). | [optional] [readonly] 
**committente** | **str** | VAT number of the Cessionario/Committente (customer). This is automatically set based on the recipient&#39;s VAT number. | [optional] [readonly] 
**prestatore** | **str** | VAT number of the Cedente/Prestatore (vendor). This is automatically set based on the sender&#39;s VAT number. | [optional] [readonly] 
**identifier** | **str** | SDI identifier. This is set by the SDI and is guaranteed to be unique within the SDI system. | [optional] [readonly] 
**file_name** | **str** | Xml file name. If not provided on send, it will be auto-generated. | [optional] 
**format** | **str** | SDI format (FPA12, FPR12, FSM10, ...) | [optional] 
**payload** | **str** | Xml payload. This is the actual xml content, as string. On send, it can be base64 encoded. If it&#39;s not, it will be encoded before sending. It is guaranteed to be encrypted at rest. | 
**last_update** | **datetime** | Last update from SDI. | [optional] [readonly] 
**date_sent** | **datetime** | When the invoice was sent to SDI. | [optional] [readonly] 
**documents** | [**List[DocumentData]**](DocumentData.md) | The invoices included in the payload. This is set by the system, based on the xml content. | [optional] [readonly] 
**encoding** | **str** | Whether the payload is Base64 encoded or a plain XML (text). | [optional] 
**nome_committente** | **str** | Business name of the committente (client/buyer) extracted from the invoice XML. | [optional] [readonly] 
**meta_data** | **Dict[str, str]** | Optional metadata, as json. | [optional] 
**latest_state** | **str** | Current SDI state of the invoice. Reflects the most recent update received from SDI. Null when no update has been received yet. | [optional] [readonly] 
**company** | [**Company**](Company.md) |  | [optional] 

## Example

```python
from invoicetronic_sdk.models.send import Send

# TODO update the JSON string below
json = "{}"
# create an instance of Send from a JSON string
send_instance = Send.from_json(json)
# print the JSON string representation of the object
print(Send.to_json())

# convert the object into a dict
send_dict = send_instance.to_dict()
# create an instance of Send from a dict
send_from_dict = Send.from_dict(send_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


