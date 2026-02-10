# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. Leave it at 0 for new records as it will be set automatically. | [optional] 
**created** | **datetime** | Creation date. It is set automatically. | [optional] 
**version** | **int** | Row version, for optimistic concurrency. It is set automatically. | [optional] 
**user_id** | **int** | User id. | [optional] 
**api_key_id** | **int** | Api key id. | [optional] 
**company_id** | **int** | Company id. | [optional] 
**method** | **str** | Request method. | 
**endpoint** | **str** | API endpoint. | 
**api_version** | **int** | Api version. | [optional] 
**status_code** | **int** | Status code returned by the API. | [optional] 
**date_time** | **datetime** | Date and time of the request. | [optional] 
**error** | **str** | Response error. | [optional] 
**resource_id** | **int** | ID of the resource created or modified by this request. | [optional] 
**success** | **bool** | Whether the request was successful. | [optional] [readonly] 
**query** | **str** | Request query. Only used for internal logging, not sent to webhooks. | [optional] 
**response_body** | **str** | Response payload. It is guaranteed to be encrypted at rest. | [optional] 

## Example

```python
from invoicetronic_sdk.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


