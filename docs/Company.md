# Company

A company model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. For POST requests, leave it at &#x60;0&#x60; — the server will assign one automatically. For PUT requests, set it to the id of the record you want to update. | [optional] 
**created** | **datetime** | Creation date. It is set automatically. | [optional] [readonly] 
**version** | **int** | Row version, for optimistic concurrency. It is set automatically. | [optional] [readonly] 
**user_id** | **int** | User id. It is set automatically based on the authenticated user. | [optional] [readonly] 
**vat** | **str** | Vat number. Must include the country code. | 
**fiscal_code** | **str** | Fiscal code. In most cases it&#39;s the same as the vat number. | 
**name** | **str** | Name | 

## Example

```python
from invoicetronic_sdk.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print(Company.to_json())

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_from_dict = Company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


