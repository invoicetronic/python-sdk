# WebHook

A webhook subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. For POST requests, leave it at &#x60;0&#x60; — the server will assign one automatically. For PUT requests, set it to the id of the record you want to update. | [optional] 
**created** | **datetime** | Creation date. It is set automatically. | [optional] [readonly] 
**version** | **int** | Row version, for optimistic concurrency. It is set automatically. | [optional] [readonly] 
**user_id** | **int** | User id. It is set automatically based on the authenticated user. | [optional] [readonly] 
**company_id** | **int** | Optional company id. If set, the webhook is restricted to events for that company; if omitted, it fires for all companies on the account. | [optional] 
**url** | **str** | The url of your application&#39;s endpoint that will receive a POST request when the webhook is fired. | 
**enabled** | **bool** | Whether the webhook is enabled. On creation, this is set to &#x60;true&#x60;. | [optional] 
**secret** | **str** | The secret used to generate webhook signatures, only returned on creation. You should store this value securely and validate it on every call, to ensure that the caller is InvoicetronicApi. | [optional] 
**description** | **str** | An optional description. | [optional] 
**events** | **List[str]** | List of events that trigger the webhook. See Invoicetronic.SupportedEvents.Available for a list of valid event names. | [optional] 
**failure_notified_at** | **datetime** | Timestamp of the last failure notification email sent for this webhook. Set by the notifier service; reset to null on successful delivery. | [optional] [readonly] 

## Example

```python
from invoicetronic_sdk.models.web_hook import WebHook

# TODO update the JSON string below
json = "{}"
# create an instance of WebHook from a JSON string
web_hook_instance = WebHook.from_json(json)
# print the JSON string representation of the object
print(WebHook.to_json())

# convert the object into a dict
web_hook_dict = web_hook_instance.to_dict()
# create an instance of WebHook from a dict
web_hook_from_dict = WebHook.from_dict(web_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


