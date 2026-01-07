# WebHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. Leave it at 0 for new records as it will be set automatically. | [optional] 
**created** | **datetime** | Creation date. It is set automatically. | [optional] 
**version** | **int** | Row version, for optimistic concurrency. It is set automatically. | [optional] 
**user_id** | **int** | User id. | [optional] 
**company_id** | **int** | Company id. | [optional] 
**url** | **str** | The url of your application&#39;s endpoint that will receive a POST request when the webhook is fired. | 
**enabled** | **bool** | Wether the webhook is enabled. On creation, this is set to &#x60;true&#x60;. | [optional] 
**secret** | **str** | The secret used to generate webhook signatures, only returned on creation. You should store this value securely and validate it on every call, to ensure that the caller is InvoicetronicApi. | [optional] 
**description** | **str** | An optional description. | [optional] 
**events** | **List[str]** | List of events to that trigger the webhook.  See Invoicetronic.SupportedEvents.Available for a list of valid event names. | [optional] 

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


