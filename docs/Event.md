# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. Leave it at 0 for new records as it will be set automatically. | [optional] 
**created** | **datetime** | Creation date. It is set automatically. | [optional] 
**version** | **int** | Row version, for optimistic concurrency. It is set automatically. | [optional] 
**company_id** | **int** | Company id. | [optional] 
**method** | **str** | Request method. | [optional] 
**query** | **str** | Request query. | [optional] 
**endpoint** | **str** | API endpoint. | [optional] 
**api_version** | **int** | Api version. | [optional] 
**status_code** | **int** | Status code returned by the API. | [optional] 
**date_time** | **datetime** | Date and time of the request. | [optional] 
**error** | **str** | Response error. | [optional] 
**request_body** | **str** | Request payload. It is guaranteed to be cyphered at rest. | [optional] 
**response_body** | **str** | Response payload. It is guaranteed to be cyphered at rest. | [optional] 
**success** | **bool** | Wether the request was successful. | [optional] [readonly] 
**user_id** | **int** | User id. | [optional] 
**api_key_id** | **int** | Api key id. | [optional] 

## Example

```python
from invoicetronic_invoice_sdk.models.event import Event

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


