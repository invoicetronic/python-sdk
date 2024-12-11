# ProblemHttpResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**problem_details** | [**ProblemDetails**](ProblemDetails.md) |  | [optional] 
**content_type** | **str** |  | [optional] [readonly] 
**status_code** | **int** |  | [optional] [readonly] 

## Example

```python
from invoicetronic_invoice_sdk.models.problem_http_result import ProblemHttpResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemHttpResult from a JSON string
problem_http_result_instance = ProblemHttpResult.from_json(json)
# print the JSON string representation of the object
print(ProblemHttpResult.to_json())

# convert the object into a dict
problem_http_result_dict = problem_http_result_instance.to_dict()
# create an instance of ProblemHttpResult from a dict
problem_http_result_from_dict = ProblemHttpResult.from_dict(problem_http_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


