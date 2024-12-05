# WebHookHistory

Webhook history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. Leave it at 0 for new records as it will be set automatically. | [optional] 
**created** | **datetime** | Creation date. It is set automatically. | [optional] 
**version** | **int** | Row version, for optimistic concurrency. It is set automatically. | [optional] 
**web_hook_id** | **int** | Webhook id. | [optional] 
**user_id** | **int** | User id. | [optional] 
**event** | **str** | Event name. | [optional] 
**status_code** | **int** | Status code. | [optional] 
**request_body** | **str** | Webhook request body. | [optional] 
**response_body** | **str** | Webhook response body. | [optional] 
**date_time** | **datetime** | Date and time of the request. | [optional] 
**success** | **bool** | Wether the request was successful. | [optional] [readonly] 

## Example

```python
from invoicetronic_invoice_sdk.models.web_hook_history import WebHookHistory

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookHistory from a JSON string
web_hook_history_instance = WebHookHistory.from_json(json)
# print the JSON string representation of the object
print(WebHookHistory.to_json())

# convert the object into a dict
web_hook_history_dict = web_hook_history_instance.to_dict()
# create an instance of WebHookHistory from a dict
web_hook_history_from_dict = WebHookHistory.from_dict(web_hook_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


