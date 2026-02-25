# SendReduced

Reduced Send data for Update responses, containing only the essential fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | SDI identifier. | [optional] 
**prestatore** | **str** | VAT number of the Cedente/Prestatore (vendor). | [optional] 
**meta_data** | **Dict[str, str]** | Optional metadata, as json. | [optional] 
**documents** | [**List[DocumentData]**](DocumentData.md) | The invoices included in the payload. | [optional] 
**date_sent** | **datetime** | When the invoice was sent to SDI. | [optional] 

## Example

```python
from invoicetronic_sdk.models.send_reduced import SendReduced

# TODO update the JSON string below
json = "{}"
# create an instance of SendReduced from a JSON string
send_reduced_instance = SendReduced.from_json(json)
# print the JSON string representation of the object
print(SendReduced.to_json())

# convert the object into a dict
send_reduced_dict = send_reduced_instance.to_dict()
# create an instance of SendReduced from a dict
send_reduced_from_dict = SendReduced.from_dict(send_reduced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


