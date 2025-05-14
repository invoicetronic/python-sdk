# invoicetronic_sdk.SendApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_file_post**](SendApi.md#send_file_post) | **POST** /send/file | Add an invoice by file
[**send_get**](SendApi.md#send_get) | **GET** /send | List invoices
[**send_id_get**](SendApi.md#send_id_get) | **GET** /send/{id} | Get a invoice by id
[**send_json_post**](SendApi.md#send_json_post) | **POST** /send/json | Add an invoice by json
[**send_post**](SendApi.md#send_post) | **POST** /send | Add an invoice
[**send_validate_file_post**](SendApi.md#send_validate_file_post) | **POST** /send/validate/file | Validate an invoice file
[**send_validate_json_post**](SendApi.md#send_validate_json_post) | **POST** /send/validate/json | Validate an invoice by json
[**send_validate_post**](SendApi.md#send_validate_post) | **POST** /send/validate | Validate an invoice
[**send_validate_xml_post**](SendApi.md#send_validate_xml_post) | **POST** /send/validate/xml | Validate an invoice by xml
[**send_xml_post**](SendApi.md#send_xml_post) | **POST** /send/xml | Add an invoice by xml


# **send_file_post**
> Send send_file_post(file, validate=validate, signature=signature)

Add an invoice by file

Send invoices are the invoices that are sent to the SDI. They are preserved for two years in the live environment and 15 days in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.send import Send
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    file = None # bytearray | 
    validate = False # bool | Validate the document first, and reject it on failure. (optional) (default to False)
    signature = Auto # str | Whether to digitally sign the document. (optional) (default to Auto)

    try:
        # Add an invoice by file
        api_response = api_instance.send_file_post(file, validate=validate, signature=signature)
        print("The response of SendApi->send_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **validate** | **bool**| Validate the document first, and reject it on failure. | [optional] [default to False]
 **signature** | **str**| Whether to digitally sign the document. | [optional] [default to Auto]

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
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_get**
> List[Send] send_get(company_id=company_id, identifier=identifier, committente=committente, prestatore=prestatore, file_name=file_name, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, document_date_from=document_date_from, document_date_to=document_date_to, document_number=document_number, page=page, page_size=page_size, sort=sort)

List invoices

test **markdown**.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.send import Send
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    company_id = 56 # int | Company id (optional)
    identifier = 'identifier_example' # str | SDI identifier. (optional)
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
        # List invoices
        api_response = api_instance.send_get(company_id=company_id, identifier=identifier, committente=committente, prestatore=prestatore, file_name=file_name, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, document_date_from=document_date_from, document_date_to=document_date_to, document_number=document_number, page=page, page_size=page_size, sort=sort)
        print("The response of SendApi->send_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Company id | [optional] 
 **identifier** | **str**| SDI identifier. | [optional] 
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

[**List[Send]**](Send.md)

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

# **send_id_get**
> Send send_id_get(id)

Get a invoice by id

Send invoices are the invoices that are sent to the SDI. They are preserved for two years in the live environment and 15 days in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.send import Send
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    id = 56 # int | Item id

    try:
        # Get a invoice by id
        api_response = api_instance.send_id_get(id)
        print("The response of SendApi->send_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

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

# **send_json_post**
> Send send_json_post(fattura_ordinaria, validate=validate, signature=signature)

Add an invoice by json

Send invoices are the invoices that are sent to the SDI. They are preserved for two years in the live environment and 15 days in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.fattura_ordinaria import FatturaOrdinaria
from invoicetronic_sdk.models.send import Send
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    fattura_ordinaria = invoicetronic_sdk.FatturaOrdinaria() # FatturaOrdinaria | 
    validate = False # bool | Validate the document first, and reject it on failure. (optional) (default to False)
    signature = Auto # str | Whether to digitally sign the document. (optional) (default to Auto)

    try:
        # Add an invoice by json
        api_response = api_instance.send_json_post(fattura_ordinaria, validate=validate, signature=signature)
        print("The response of SendApi->send_json_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send_json_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fattura_ordinaria** | [**FatturaOrdinaria**](FatturaOrdinaria.md)|  | 
 **validate** | **bool**| Validate the document first, and reject it on failure. | [optional] [default to False]
 **signature** | **str**| Whether to digitally sign the document. | [optional] [default to Auto]

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
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_post**
> Send send_post(send, validate=validate, signature=signature)

Add an invoice

Send invoices are the invoices that are sent to the SDI. They are preserved for two years in the live environment and 15 days in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.send import Send
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    send = invoicetronic_sdk.Send() # Send | 
    validate = False # bool | Validate the document first, and reject it on failure. (optional) (default to False)
    signature = Auto # str | Whether to digitally sign the document. (optional) (default to Auto)

    try:
        # Add an invoice
        api_response = api_instance.send_post(send, validate=validate, signature=signature)
        print("The response of SendApi->send_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send** | [**Send**](Send.md)|  | 
 **validate** | **bool**| Validate the document first, and reject it on failure. | [optional] [default to False]
 **signature** | **str**| Whether to digitally sign the document. | [optional] [default to Auto]

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
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_validate_file_post**
> send_validate_file_post(file)

Validate an invoice file

Send invoices are the invoices that are sent to the SDI. They are preserved for two years in the live environment and 15 days in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    file = None # bytearray | 

    try:
        # Validate an invoice file
        api_instance.send_validate_file_post(file)
    except Exception as e:
        print("Exception when calling SendApi->send_validate_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_validate_json_post**
> send_validate_json_post(fattura_ordinaria)

Validate an invoice by json

Send invoices are the invoices that are sent to the SDI. They are preserved for two years in the live environment and 15 days in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.fattura_ordinaria import FatturaOrdinaria
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    fattura_ordinaria = invoicetronic_sdk.FatturaOrdinaria() # FatturaOrdinaria | 

    try:
        # Validate an invoice by json
        api_instance.send_validate_json_post(fattura_ordinaria)
    except Exception as e:
        print("Exception when calling SendApi->send_validate_json_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fattura_ordinaria** | [**FatturaOrdinaria**](FatturaOrdinaria.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_validate_post**
> send_validate_post(send)

Validate an invoice

Send invoices are the invoices that are sent to the SDI. They are preserved for two years in the live environment and 15 days in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.send import Send
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    send = invoicetronic_sdk.Send() # Send | 

    try:
        # Validate an invoice
        api_instance.send_validate_post(send)
    except Exception as e:
        print("Exception when calling SendApi->send_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send** | [**Send**](Send.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_validate_xml_post**
> send_validate_xml_post(fattura_ordinaria)

Validate an invoice by xml

Send invoices are the invoices that are sent to the SDI. They are preserved for two years in the live environment and 15 days in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.fattura_ordinaria import FatturaOrdinaria
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    fattura_ordinaria = invoicetronic_sdk.FatturaOrdinaria() # FatturaOrdinaria | 

    try:
        # Validate an invoice by xml
        api_instance.send_validate_xml_post(fattura_ordinaria)
    except Exception as e:
        print("Exception when calling SendApi->send_validate_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fattura_ordinaria** | [**FatturaOrdinaria**](FatturaOrdinaria.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_xml_post**
> Send send_xml_post(fattura_ordinaria, validate=validate, signature=signature)

Add an invoice by xml

Send invoices are the invoices that are sent to the SDI. They are preserved for two years in the live environment and 15 days in the Sandbox.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.fattura_ordinaria import FatturaOrdinaria
from invoicetronic_sdk.models.send import Send
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = invoicetronic_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.SendApi(api_client)
    fattura_ordinaria = invoicetronic_sdk.FatturaOrdinaria() # FatturaOrdinaria | 
    validate = False # bool | Validate the document first, and reject it on failure. (optional) (default to False)
    signature = Auto # str | Whether to digitally sign the document. (optional) (default to Auto)

    try:
        # Add an invoice by xml
        api_response = api_instance.send_xml_post(fattura_ordinaria, validate=validate, signature=signature)
        print("The response of SendApi->send_xml_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fattura_ordinaria** | [**FatturaOrdinaria**](FatturaOrdinaria.md)|  | 
 **validate** | **bool**| Validate the document first, and reject it on failure. | [optional] [default to False]
 **signature** | **str**| Whether to digitally sign the document. | [optional] [default to Auto]

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
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

