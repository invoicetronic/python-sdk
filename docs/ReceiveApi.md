# invoicetronic_invoice_sdk.ReceiveApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receive_get**](ReceiveApi.md#receive_get) | **GET** /receive | List incoming invoices
[**receive_id_delete**](ReceiveApi.md#receive_id_delete) | **DELETE** /receive/{id} | Delete an incoming invoice by id
[**receive_id_get**](ReceiveApi.md#receive_id_get) | **GET** /receive/{id} | Get an incoming invoice by id


# **receive_get**
> List[Receive] receive_get(company_id=company_id, identifier=identifier, unread=unread, committente=committente, prestatore=prestatore, file_name=file_name, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, document_date_from=document_date_from, document_date_to=document_date_to, document_number=document_number, page=page, page_size=page_size, sort=sort)

List incoming invoices

Receive invoices are the invoices that are received from other companies. They are preserved for two years in the live environment and 24 hours in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.receive import Receive
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
    api_instance = invoicetronic_invoice_sdk.ReceiveApi(api_client)
    company_id = 56 # int | Company id (optional)
    identifier = 'identifier_example' # str | SDI identifier. (optional)
    unread = True # bool | Unread items only. (optional)
    committente = 'committente_example' # str | Vat number or fiscal code. (optional)
    prestatore = 'prestatore_example' # str | Vat number or fiscal code. (optional)
    file_name = 'file_name_example' # str | File name. (optional)
    last_update_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    last_update_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    date_sent_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    date_sent_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    document_date_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    document_date_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    document_number = 'document_number_example' # str | Document number. (optional)
    page = 1 # int | Page number. Defaults to 1. (optional) (default to 1)
    page_size = 100 # int | Items per page. Defaults to 50. Cannot be greater than 200. (optional) (default to 100)
    sort = 'sort_example' # str | Sort by field. Prefix with '-' for descending order. (optional)

    try:
        # List incoming invoices
        api_response = api_instance.receive_get(company_id=company_id, identifier=identifier, unread=unread, committente=committente, prestatore=prestatore, file_name=file_name, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, document_date_from=document_date_from, document_date_to=document_date_to, document_number=document_number, page=page, page_size=page_size, sort=sort)
        print("The response of ReceiveApi->receive_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiveApi->receive_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Company id | [optional] 
 **identifier** | **str**| SDI identifier. | [optional] 
 **unread** | **bool**| Unread items only. | [optional] 
 **committente** | **str**| Vat number or fiscal code. | [optional] 
 **prestatore** | **str**| Vat number or fiscal code. | [optional] 
 **file_name** | **str**| File name. | [optional] 
 **last_update_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **last_update_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **date_sent_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **date_sent_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **document_date_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **document_date_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **document_number** | **str**| Document number. | [optional] 
 **page** | **int**| Page number. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| Items per page. Defaults to 50. Cannot be greater than 200. | [optional] [default to 100]
 **sort** | **str**| Sort by field. Prefix with &#39;-&#39; for descending order. | [optional] 

### Return type

[**List[Receive]**](Receive.md)

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

# **receive_id_delete**
> Receive receive_id_delete(id)

Delete an incoming invoice by id

Receive invoices are the invoices that are received from other companies. They are preserved for two years in the live environment and 24 hours in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.receive import Receive
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
    api_instance = invoicetronic_invoice_sdk.ReceiveApi(api_client)
    id = 56 # int | Item id

    try:
        # Delete an incoming invoice by id
        api_response = api_instance.receive_id_delete(id)
        print("The response of ReceiveApi->receive_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiveApi->receive_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**Receive**](Receive.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_id_get**
> Receive receive_id_get(id)

Get an incoming invoice by id

Receive invoices are the invoices that are received from other companies. They are preserved for two years in the live environment and 24 hours in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.receive import Receive
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
    api_instance = invoicetronic_invoice_sdk.ReceiveApi(api_client)
    id = 56 # int | Item id

    try:
        # Get an incoming invoice by id
        api_response = api_instance.receive_id_get(id)
        print("The response of ReceiveApi->receive_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiveApi->receive_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**Receive**](Receive.md)

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

