# invoicetronic_invoice_sdk.LogApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_get**](LogApi.md#log_get) | **GET** /log | List events
[**log_id_get**](LogApi.md#log_id_get) | **GET** /log/{id} | Get an event by id


# **log_get**
> List[Event] log_get(company_id=company_id, endpoint=endpoint, method=method, api_verion=api_verion, status_code=status_code, date_created_from=date_created_from, date_created_to=date_created_to, page=page, page_size=page_size, sort=sort, query=query, success=success, date_time_from=date_time_from, date_time_to=date_time_to)

List events

Every API operation is logged and can be retrieved here. Log records are preserved for 15 days.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.event import Event
from invoicetronic_invoice_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_invoice_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_invoice_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_invoice_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_invoice_sdk.LogApi(api_client)
    company_id = 56 # int | Company id (optional)
    endpoint = 'endpoint_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    api_verion = 56 # int | Api version (optional)
    status_code = 56 # int | Response status code (optional)
    date_created_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    date_created_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    page = 1 # int | Page number. Defaults to 1. (optional) (default to 1)
    page_size = 100 # int | Items per page. Defaults to 50. Cannot be greater than 200. (optional) (default to 100)
    sort = 'sort_example' # str | Sort by field. Prefix with '-' for descending order. (optional)
    query = 'query_example' # str |  (optional)
    success = True # bool |  (optional)
    date_time_from = '2013-10-20T19:20:30+01:00' # datetime | Date and time of the event (optional)
    date_time_to = '2013-10-20T19:20:30+01:00' # datetime | Date and time of the event (optional)

    try:
        # List events
        api_response = api_instance.log_get(company_id=company_id, endpoint=endpoint, method=method, api_verion=api_verion, status_code=status_code, date_created_from=date_created_from, date_created_to=date_created_to, page=page, page_size=page_size, sort=sort, query=query, success=success, date_time_from=date_time_from, date_time_to=date_time_to)
        print("The response of LogApi->log_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogApi->log_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Company id | [optional] 
 **endpoint** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **api_verion** | **int**| Api version | [optional] 
 **status_code** | **int**| Response status code | [optional] 
 **date_created_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **date_created_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **page** | **int**| Page number. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| Items per page. Defaults to 50. Cannot be greater than 200. | [optional] [default to 100]
 **sort** | **str**| Sort by field. Prefix with &#39;-&#39; for descending order. | [optional] 
 **query** | **str**|  | [optional] 
 **success** | **bool**|  | [optional] 
 **date_time_from** | **datetime**| Date and time of the event | [optional] 
 **date_time_to** | **datetime**| Date and time of the event | [optional] 

### Return type

[**List[Event]**](Event.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_id_get**
> Event log_id_get(id)

Get an event by id

Every API operation is logged and can be retrieved here. Log records are preserved for 15 days.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.event import Event
from invoicetronic_invoice_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_invoice_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_invoice_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_invoice_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_invoice_sdk.LogApi(api_client)
    id = 56 # int | Item id

    try:
        # Get an event by id
        api_response = api_instance.log_id_get(id)
        print("The response of LogApi->log_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogApi->log_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**Event**](Event.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

