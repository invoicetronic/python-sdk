# invoicetronic_invoice_sdk.SendApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoice_v1_send_files_post**](SendApi.md#invoice_v1_send_files_post) | **POST** /invoice/v1/send/files | Add a send invoice by file
[**invoice_v1_send_get**](SendApi.md#invoice_v1_send_get) | **GET** /invoice/v1/send | List send invoices
[**invoice_v1_send_id_get**](SendApi.md#invoice_v1_send_id_get) | **GET** /invoice/v1/send/{id} | Get a send invoice by id
[**invoice_v1_send_json_post**](SendApi.md#invoice_v1_send_json_post) | **POST** /invoice/v1/send/json | Add a send invoice by json
[**invoice_v1_send_post**](SendApi.md#invoice_v1_send_post) | **POST** /invoice/v1/send | Add a send invoice
[**invoice_v1_send_xml_post**](SendApi.md#invoice_v1_send_xml_post) | **POST** /invoice/v1/send/xml | Add a send invoice by xml


# **invoice_v1_send_files_post**
> Send invoice_v1_send_files_post(files, validate=validate)

Add a send invoice by file

Send invoices are the invoices that are sent to the SDI.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.send import Send
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
    api_instance = invoicetronic_invoice_sdk.SendApi(api_client)
    files = None # List[bytearray] | 
    validate = False # bool | Validate the document first, and reject it on failure. (optional) (default to False)

    try:
        # Add a send invoice by file
        api_response = api_instance.invoice_v1_send_files_post(files, validate=validate)
        print("The response of SendApi->invoice_v1_send_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->invoice_v1_send_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **List[bytearray]**|  | 
 **validate** | **bool**| Validate the document first, and reject it on failure. | [optional] [default to False]

### Return type

[**Send**](Send.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_v1_send_get**
> List[Send] invoice_v1_send_get(company_id=company_id, identifier=identifier, committente=committente, prestatore=prestatore, file_name=file_name, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, document_date_from=document_date_from, document_date_to=document_date_to, document_number=document_number, page=page, page_size=page_size)

List send invoices

test **markdown**.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.send import Send
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
    api_instance = invoicetronic_invoice_sdk.SendApi(api_client)
    company_id = 56 # int | Company id. (optional)
    identifier = 'identifier_example' # str | SDI identifier. (optional)
    committente = 'committente_example' # str | VAT number or fiscal code. (optional)
    prestatore = 'prestatore_example' # str | VAT number or fiscal code. (optional)
    file_name = 'file_name_example' # str | File name. (optional)
    last_update_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    last_update_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    date_sent_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    date_sent_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    document_date_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    document_date_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    document_number = 'document_number_example' # str | Document number. (optional)
    page = 1 # int | Page number. (optional) (default to 1)
    page_size = 100 # int | Items per page. (optional) (default to 100)

    try:
        # List send invoices
        api_response = api_instance.invoice_v1_send_get(company_id=company_id, identifier=identifier, committente=committente, prestatore=prestatore, file_name=file_name, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, document_date_from=document_date_from, document_date_to=document_date_to, document_number=document_number, page=page, page_size=page_size)
        print("The response of SendApi->invoice_v1_send_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->invoice_v1_send_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Company id. | [optional] 
 **identifier** | **str**| SDI identifier. | [optional] 
 **committente** | **str**| VAT number or fiscal code. | [optional] 
 **prestatore** | **str**| VAT number or fiscal code. | [optional] 
 **file_name** | **str**| File name. | [optional] 
 **last_update_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **last_update_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **date_sent_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **date_sent_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **document_date_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **document_date_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **document_number** | **str**| Document number. | [optional] 
 **page** | **int**| Page number. | [optional] [default to 1]
 **page_size** | **int**| Items per page. | [optional] [default to 100]

### Return type

[**List[Send]**](Send.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_v1_send_id_get**
> Send invoice_v1_send_id_get(id)

Get a send invoice by id

Send invoices are the invoices that are sent to the SDI.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.send import Send
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
    api_instance = invoicetronic_invoice_sdk.SendApi(api_client)
    id = 56 # int | Item id.

    try:
        # Get a send invoice by id
        api_response = api_instance.invoice_v1_send_id_get(id)
        print("The response of SendApi->invoice_v1_send_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->invoice_v1_send_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id. | 

### Return type

[**Send**](Send.md)

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

# **invoice_v1_send_json_post**
> Send invoice_v1_send_json_post(fattura_ordinaria, validate=validate)

Add a send invoice by json

Send invoices are the invoices that are sent to the SDI.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.fattura_ordinaria import FatturaOrdinaria
from invoicetronic_invoice_sdk.models.send import Send
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
    api_instance = invoicetronic_invoice_sdk.SendApi(api_client)
    fattura_ordinaria = invoicetronic_invoice_sdk.FatturaOrdinaria() # FatturaOrdinaria | 
    validate = False # bool | Validate the document first, and reject it on failure. (optional) (default to False)

    try:
        # Add a send invoice by json
        api_response = api_instance.invoice_v1_send_json_post(fattura_ordinaria, validate=validate)
        print("The response of SendApi->invoice_v1_send_json_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->invoice_v1_send_json_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fattura_ordinaria** | [**FatturaOrdinaria**](FatturaOrdinaria.md)|  | 
 **validate** | **bool**| Validate the document first, and reject it on failure. | [optional] [default to False]

### Return type

[**Send**](Send.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_v1_send_post**
> Send invoice_v1_send_post(send, validate=validate)

Add a send invoice

Send invoices are the invoices that are sent to the SDI.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.send import Send
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
    api_instance = invoicetronic_invoice_sdk.SendApi(api_client)
    send = invoicetronic_invoice_sdk.Send() # Send | 
    validate = False # bool | Validate the document first, and reject it on failure. (optional) (default to False)

    try:
        # Add a send invoice
        api_response = api_instance.invoice_v1_send_post(send, validate=validate)
        print("The response of SendApi->invoice_v1_send_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->invoice_v1_send_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send** | [**Send**](Send.md)|  | 
 **validate** | **bool**| Validate the document first, and reject it on failure. | [optional] [default to False]

### Return type

[**Send**](Send.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_v1_send_xml_post**
> Send invoice_v1_send_xml_post(fattura_ordinaria, validate=validate)

Add a send invoice by xml

Send invoices are the invoices that are sent to the SDI.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.fattura_ordinaria import FatturaOrdinaria
from invoicetronic_invoice_sdk.models.send import Send
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
    api_instance = invoicetronic_invoice_sdk.SendApi(api_client)
    fattura_ordinaria = invoicetronic_invoice_sdk.FatturaOrdinaria() # FatturaOrdinaria | 
    validate = False # bool | Validate the document first, and reject it on failure. (optional) (default to False)

    try:
        # Add a send invoice by xml
        api_response = api_instance.invoice_v1_send_xml_post(fattura_ordinaria, validate=validate)
        print("The response of SendApi->invoice_v1_send_xml_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->invoice_v1_send_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fattura_ordinaria** | [**FatturaOrdinaria**](FatturaOrdinaria.md)|  | 
 **validate** | **bool**| Validate the document first, and reject it on failure. | [optional] [default to False]

### Return type

[**Send**](Send.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

