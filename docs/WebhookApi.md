# invoicetronic_invoice_sdk.WebhookApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoice_v1_webhook_get**](WebhookApi.md#invoice_v1_webhook_get) | **GET** /invoice/v1/webhook | List webhooks
[**invoice_v1_webhook_id_delete**](WebhookApi.md#invoice_v1_webhook_id_delete) | **DELETE** /invoice/v1/webhook/{id} | Delete a webhook by id
[**invoice_v1_webhook_id_get**](WebhookApi.md#invoice_v1_webhook_id_get) | **GET** /invoice/v1/webhook/{id} | Get a webhook by id
[**invoice_v1_webhook_post**](WebhookApi.md#invoice_v1_webhook_post) | **POST** /invoice/v1/webhook | Add a webhook
[**invoice_v1_webhook_put**](WebhookApi.md#invoice_v1_webhook_put) | **PUT** /invoice/v1/webhook | Update a webhook
[**invoice_v1_webhookhistory_get**](WebhookApi.md#invoice_v1_webhookhistory_get) | **GET** /invoice/v1/webhookhistory | List webhook history items
[**invoice_v1_webhookhistory_id_get**](WebhookApi.md#invoice_v1_webhookhistory_id_get) | **GET** /invoice/v1/webhookhistory/{id} | Get a webhook history item by id


# **invoice_v1_webhook_get**
> List[WebHook] invoice_v1_webhook_get(page=page, page_size=page_size)

List webhooks

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_invoice_sdk.WebhookApi(api_client)
    page = 1 # int | Page number. Defaults to 1. (optional) (default to 1)
    page_size = 100 # int | Items per page. Defaults to 50. Cannot be greater than 200. (optional) (default to 100)

    try:
        # List webhooks
        api_response = api_instance.invoice_v1_webhook_get(page=page, page_size=page_size)
        print("The response of WebhookApi->invoice_v1_webhook_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->invoice_v1_webhook_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| Items per page. Defaults to 50. Cannot be greater than 200. | [optional] [default to 100]

### Return type

[**List[WebHook]**](WebHook.md)

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

# **invoice_v1_webhook_id_delete**
> WebHook invoice_v1_webhook_id_delete(id)

Delete a webhook by id

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_invoice_sdk.WebhookApi(api_client)
    id = 56 # int | Item id

    try:
        # Delete a webhook by id
        api_response = api_instance.invoice_v1_webhook_id_delete(id)
        print("The response of WebhookApi->invoice_v1_webhook_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->invoice_v1_webhook_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**WebHook**](WebHook.md)

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

# **invoice_v1_webhook_id_get**
> WebHook invoice_v1_webhook_id_get(id)

Get a webhook by id

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_invoice_sdk.WebhookApi(api_client)
    id = 56 # int | Item id

    try:
        # Get a webhook by id
        api_response = api_instance.invoice_v1_webhook_id_get(id)
        print("The response of WebhookApi->invoice_v1_webhook_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->invoice_v1_webhook_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**WebHook**](WebHook.md)

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

# **invoice_v1_webhook_post**
> WebHook invoice_v1_webhook_post(web_hook)

Add a webhook

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_invoice_sdk.WebhookApi(api_client)
    web_hook = invoicetronic_invoice_sdk.WebHook() # WebHook | 

    try:
        # Add a webhook
        api_response = api_instance.invoice_v1_webhook_post(web_hook)
        print("The response of WebhookApi->invoice_v1_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->invoice_v1_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook** | [**WebHook**](WebHook.md)|  | 

### Return type

[**WebHook**](WebHook.md)

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

# **invoice_v1_webhook_put**
> WebHook invoice_v1_webhook_put(web_hook)

Update a webhook

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_invoice_sdk.WebhookApi(api_client)
    web_hook = invoicetronic_invoice_sdk.WebHook() # WebHook | 

    try:
        # Update a webhook
        api_response = api_instance.invoice_v1_webhook_put(web_hook)
        print("The response of WebhookApi->invoice_v1_webhook_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->invoice_v1_webhook_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook** | [**WebHook**](WebHook.md)|  | 

### Return type

[**WebHook**](WebHook.md)

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

# **invoice_v1_webhookhistory_get**
> List[WebHookHistory] invoice_v1_webhookhistory_get(page=page, page_size=page_size)

List webhook history items

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.web_hook_history import WebHookHistory
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
    api_instance = invoicetronic_invoice_sdk.WebhookApi(api_client)
    page = 1 # int | Page number. Defaults to 1. (optional) (default to 1)
    page_size = 100 # int | Items per page. Defaults to 50. Cannot be greater than 200. (optional) (default to 100)

    try:
        # List webhook history items
        api_response = api_instance.invoice_v1_webhookhistory_get(page=page, page_size=page_size)
        print("The response of WebhookApi->invoice_v1_webhookhistory_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->invoice_v1_webhookhistory_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| Items per page. Defaults to 50. Cannot be greater than 200. | [optional] [default to 100]

### Return type

[**List[WebHookHistory]**](WebHookHistory.md)

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

# **invoice_v1_webhookhistory_id_get**
> WebHookHistory invoice_v1_webhookhistory_id_get(id)

Get a webhook history item by id

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_invoice_sdk
from invoicetronic_invoice_sdk.models.web_hook_history import WebHookHistory
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
    api_instance = invoicetronic_invoice_sdk.WebhookApi(api_client)
    id = 56 # int | Item id

    try:
        # Get a webhook history item by id
        api_response = api_instance.invoice_v1_webhookhistory_id_get(id)
        print("The response of WebhookApi->invoice_v1_webhookhistory_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->invoice_v1_webhookhistory_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**WebHookHistory**](WebHookHistory.md)

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

