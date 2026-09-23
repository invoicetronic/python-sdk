# Permissions

Permissions of a restricted key, per resource. A missing property means no access to that resource. Each permission cannot exceed the one of the main key the restricted key belongs to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** | Companies: &#x60;Read&#x60; lists and reads them, &#x60;Write&#x60; also creates, updates and deletes them. | [optional] 
**send** | **str** | Outgoing invoices: &#x60;Read&#x60; lists and reads them, &#x60;Write&#x60; also sends and validates invoices. | [optional] 
**receive** | **str** | Incoming invoices: &#x60;Read&#x60; lists and reads them, &#x60;Write&#x60; also deletes them. | [optional] 
**webhook** | **str** | Webhooks: &#x60;Read&#x60; lists and reads them, &#x60;Write&#x60; also creates, updates and deletes them. | [optional] 
**update** | **str** | SDI status updates of outgoing invoices. | [optional] 
**log** | **str** | Event log. | [optional] 
**webhookhistory** | **str** | Webhook delivery history. | [optional] 
**export** | **str** | Invoice export. | [optional] 
**status** | **str** | Account status (remaining operations and signatures). | [optional] 

## Example

```python
from invoicetronic_sdk.models.permissions import Permissions

# TODO update the JSON string below
json = "{}"
# create an instance of Permissions from a JSON string
permissions_instance = Permissions.from_json(json)
# print the JSON string representation of the object
print(Permissions.to_json())

# convert the object into a dict
permissions_dict = permissions_instance.to_dict()
# create an instance of Permissions from a dict
permissions_from_dict = Permissions.from_dict(permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


