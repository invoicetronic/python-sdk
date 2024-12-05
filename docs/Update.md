# Update


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. Leave it at 0 for new records as it will be set automatically. | [optional] 
**created** | **datetime** | Creation date. It is set automatically. | [optional] 
**version** | **int** | Row version, for optimistic concurrency. It is set automatically. | [optional] 
**user_id** | **int** | User id. | [optional] 
**company_id** | **int** | Company id. | [optional] 
**send_id** | **int** | Send id. This is the id of the sent invoice to which this update refers to. | [optional] 
**date_sent** | **datetime** | When the document was sent to the SDI. | [optional] 
**last_update** | **datetime** | Last update from SDI. | [optional] 
**identifier** | **str** | SDI identifier. This is set by the SDI and it is unique within the SDI system. | [optional] 
**state** | **str** | State of the document. Theses are the possible values, as per the SDI documentation: | [optional] 
**description** | **str** | Description for the state. | [optional] 
**message_id** | **str** | SDI message id. | [optional] 
**errors** | [**List[Error]**](Error.md) | SDI errors, if any. | [optional] 
**is_read** | **bool** | Wether the item has been read at least once. | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.update import Update

# TODO update the JSON string below
json = "{}"
# create an instance of Update from a JSON string
update_instance = Update.from_json(json)
# print the JSON string representation of the object
print(Update.to_json())

# convert the object into a dict
update_dict = update_instance.to_dict()
# create an instance of Update from a dict
update_from_dict = Update.from_dict(update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


