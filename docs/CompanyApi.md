# invoicetronic_invoice_sdk.CompanyApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_get**](CompanyApi.md#company_get) | **GET** /company | List companies
[**company_id_delete**](CompanyApi.md#company_id_delete) | **DELETE** /company/{id} | Delete a company
[**company_id_get**](CompanyApi.md#company_id_get) | **GET** /company/{id} | Get a company by id
[**company_post**](CompanyApi.md#company_post) | **POST** /company | Add a company
[**company_put**](CompanyApi.md#company_put) | **PUT** /company | Update a company


# **company_get**
> List[Company] company_get(page=page, page_size=page_size, sort=sort)

List companies

Companies are the entities that send and receive invoices. As you send invoices, companies are added as needed. **You can only receive invoices for existing companies**.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.company import Company
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
    api_instance = invoicetronic_invoice_sdk.CompanyApi(api_client)
    page = 1 # int | Page number. Defaults to 1. (optional) (default to 1)
    page_size = 100 # int | Items per page. Defaults to 50. Cannot be greater than 200. (optional) (default to 100)
    sort = 'sort_example' # str | Sort by field. Prefix with '-' for descending order. (optional)

    try:
        # List companies
        api_response = api_instance.company_get(page=page, page_size=page_size, sort=sort)
        print("The response of CompanyApi->company_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| Items per page. Defaults to 50. Cannot be greater than 200. | [optional] [default to 100]
 **sort** | **str**| Sort by field. Prefix with &#39;-&#39; for descending order. | [optional] 

### Return type

[**List[Company]**](Company.md)

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

# **company_id_delete**
> Company company_id_delete(id)

Delete a company

Companies are the entities that send and receive invoices. As you send invoices, companies are added as needed. **You can only receive invoices for existing companies**.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.company import Company
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
    api_instance = invoicetronic_invoice_sdk.CompanyApi(api_client)
    id = 56 # int | Item id

    try:
        # Delete a company
        api_response = api_instance.company_id_delete(id)
        print("The response of CompanyApi->company_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**Company**](Company.md)

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

# **company_id_get**
> Company company_id_get(id)

Get a company by id

Companies are the entities that send and receive invoices. As you send invoices, companies are added as needed. **You can only receive invoices for existing companies**.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.company import Company
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
    api_instance = invoicetronic_invoice_sdk.CompanyApi(api_client)
    id = 56 # int | Item id

    try:
        # Get a company by id
        api_response = api_instance.company_id_get(id)
        print("The response of CompanyApi->company_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**Company**](Company.md)

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

# **company_post**
> Company company_post(company)

Add a company

Companies are the entities that send and receive invoices. As you send invoices, companies are added as needed. **You can only receive invoices for existing companies**.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.company import Company
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
    api_instance = invoicetronic_invoice_sdk.CompanyApi(api_client)
    company = invoicetronic_invoice_sdk.Company() # Company | 

    try:
        # Add a company
        api_response = api_instance.company_post(company)
        print("The response of CompanyApi->company_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | [**Company**](Company.md)|  | 

### Return type

[**Company**](Company.md)

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

# **company_put**
> Company company_put(company)

Update a company

Companies are the entities that send and receive invoices. As you send invoices, companies are added as needed. **You can only receive invoices for existing companies**.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.company import Company
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
    api_instance = invoicetronic_invoice_sdk.CompanyApi(api_client)
    company = invoicetronic_invoice_sdk.Company() # Company | 

    try:
        # Update a company
        api_response = api_instance.company_put(company)
        print("The response of CompanyApi->company_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | [**Company**](Company.md)|  | 

### Return type

[**Company**](Company.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Content |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

