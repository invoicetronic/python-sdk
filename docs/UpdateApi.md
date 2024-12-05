# invoicetronic_invoice_sdk.UpdateApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoice_v1_update_get**](UpdateApi.md#invoice_v1_update_get) | **GET** /invoice/v1/update | List updates
[**invoice_v1_update_id_get**](UpdateApi.md#invoice_v1_update_id_get) | **GET** /invoice/v1/update/{id} | Get an update by id


# **invoice_v1_update_get**
> List[Update] invoice_v1_update_get(company_id=company_id, identifier=identifier, unread=unread, send_id=send_id, state=state, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, page=page, page_size=page_size)

List updates

Updates are notifications that are sent by the SDI about the status of sent invoices.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.update import Update
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
    api_instance = invoicetronic_invoice_sdk.UpdateApi(api_client)
    company_id = 56 # int | Company id. (optional)
    identifier = 'identifier_example' # str | SDI identifier. (optional)
    unread = True # bool | Only unread items. (optional)
    send_id = 56 # int | Send item's id. (optional)
    state = 'state_example' # str | SDI state (optional)
    last_update_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    last_update_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    date_sent_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    date_sent_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 format (2024-11-29T12:34:56Z) (optional)
    page = 1 # int | Page number. (optional) (default to 1)
    page_size = 100 # int | Items per page. (optional) (default to 100)

    try:
        # List updates
        api_response = api_instance.invoice_v1_update_get(company_id=company_id, identifier=identifier, unread=unread, send_id=send_id, state=state, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, page=page, page_size=page_size)
        print("The response of UpdateApi->invoice_v1_update_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateApi->invoice_v1_update_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Company id. | [optional] 
 **identifier** | **str**| SDI identifier. | [optional] 
 **unread** | **bool**| Only unread items. | [optional] 
 **send_id** | **int**| Send item&#39;s id. | [optional] 
 **state** | **str**| SDI state | [optional] 
 **last_update_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **last_update_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **date_sent_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **date_sent_to** | **datetime**| UTC ISO 8601 format (2024-11-29T12:34:56Z) | [optional] 
 **page** | **int**| Page number. | [optional] [default to 1]
 **page_size** | **int**| Items per page. | [optional] [default to 100]

### Return type

[**List[Update]**](Update.md)

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

# **invoice_v1_update_id_get**
> Update invoice_v1_update_id_get(id)

Get an update by id

Updates are notifications that are sent by the SDI about the status of sent invoices.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.update import Update
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
    api_instance = invoicetronic_invoice_sdk.UpdateApi(api_client)
    id = 56 # int | Item id.

    try:
        # Get an update by id
        api_response = api_instance.invoice_v1_update_id_get(id)
        print("The response of UpdateApi->invoice_v1_update_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateApi->invoice_v1_update_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id. | 

### Return type

[**Update**](Update.md)

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

