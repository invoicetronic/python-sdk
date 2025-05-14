# invoicetronic_sdk.WebhookApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_get**](WebhookApi.md#webhook_get) | **GET** /webhook | List webhooks
[**webhook_id_delete**](WebhookApi.md#webhook_id_delete) | **DELETE** /webhook/{id} | Delete a webhook by id
[**webhook_id_get**](WebhookApi.md#webhook_id_get) | **GET** /webhook/{id} | Get a webhook by id
[**webhook_post**](WebhookApi.md#webhook_post) | **POST** /webhook | Add a webhook
[**webhook_put**](WebhookApi.md#webhook_put) | **PUT** /webhook | Update a webhook
[**webhookhistory_get**](WebhookApi.md#webhookhistory_get) | **GET** /webhookhistory | List webhook history items
[**webhookhistory_id_get**](WebhookApi.md#webhookhistory_id_get) | **GET** /webhookhistory/{id} | Get a webhook history item by id


# **webhook_get**
> List[WebHook] webhook_get(company_id=company_id, page=page, page_size=page_size, sort=sort, description=description, enabled=enabled, events=events, url=url)

List webhooks

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_sdk.WebhookApi(api_client)
    company_id = 56 # int | Company id (optional)
    page = 1 # int | Page number. Defaults to 1. (optional) (default to 1)
    page_size = 100 # int | Items per page. Defaults to 50. Cannot be greater than 200. (optional) (default to 100)
    sort = 'sort_example' # str | Sort by field. Prefix with '-' for descending order. (optional)
    description = 'description_example' # str |  (optional)
    enabled = True # bool |  (optional)
    events = 'events_example' # str |  (optional)
    url = 'url_example' # str |  (optional)

    try:
        # List webhooks
        api_response = api_instance.webhook_get(company_id=company_id, page=page, page_size=page_size, sort=sort, description=description, enabled=enabled, events=events, url=url)
        print("The response of WebhookApi->webhook_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Company id | [optional] 
 **page** | **int**| Page number. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| Items per page. Defaults to 50. Cannot be greater than 200. | [optional] [default to 100]
 **sort** | **str**| Sort by field. Prefix with &#39;-&#39; for descending order. | [optional] 
 **description** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **events** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 

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

# **webhook_id_delete**
> WebHook webhook_id_delete(id)

Delete a webhook by id

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_sdk.WebhookApi(api_client)
    id = 56 # int | Item id

    try:
        # Delete a webhook by id
        api_response = api_instance.webhook_id_delete(id)
        print("The response of WebhookApi->webhook_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_id_delete: %s\n" % e)
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

# **webhook_id_get**
> WebHook webhook_id_get(id)

Get a webhook by id

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_sdk.WebhookApi(api_client)
    id = 56 # int | Item id

    try:
        # Get a webhook by id
        api_response = api_instance.webhook_id_get(id)
        print("The response of WebhookApi->webhook_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_id_get: %s\n" % e)
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

# **webhook_post**
> WebHook webhook_post(web_hook)

Add a webhook

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_sdk.WebhookApi(api_client)
    web_hook = invoicetronic_sdk.WebHook() # WebHook | 

    try:
        # Add a webhook
        api_response = api_instance.webhook_post(web_hook)
        print("The response of WebhookApi->webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_post: %s\n" % e)
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

# **webhook_put**
> WebHook webhook_put(web_hook)

Update a webhook

Webhooks are used to notify external services about write events that occur in the API. You can subscribe to specific events and receive a notification when they occur.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.web_hook import WebHook
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
    api_instance = invoicetronic_sdk.WebhookApi(api_client)
    web_hook = invoicetronic_sdk.WebHook() # WebHook | 

    try:
        # Update a webhook
        api_response = api_instance.webhook_put(web_hook)
        print("The response of WebhookApi->webhook_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_put: %s\n" % e)
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

# **webhookhistory_get**
> List[WebHookHistory] webhookhistory_get(page=page, page_size=page_size, sort=sort, webhook_id=webhook_id)

List webhook history items

Webhook history items are stored in the database and can be accessed via the API. They are preserved for 15 in both the live and sandbox environments.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.web_hook_history import WebHookHistory
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
    api_instance = invoicetronic_sdk.WebhookApi(api_client)
    page = 1 # int | Page number. Defaults to 1. (optional) (default to 1)
    page_size = 100 # int | Items per page. Defaults to 50. Cannot be greater than 200. (optional) (default to 100)
    sort = 'sort_example' # str | Sort by field. Prefix with '-' for descending order. (optional)
    webhook_id = 56 # int | WebHook id (optional)

    try:
        # List webhook history items
        api_response = api_instance.webhookhistory_get(page=page, page_size=page_size, sort=sort, webhook_id=webhook_id)
        print("The response of WebhookApi->webhookhistory_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhookhistory_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| Items per page. Defaults to 50. Cannot be greater than 200. | [optional] [default to 100]
 **sort** | **str**| Sort by field. Prefix with &#39;-&#39; for descending order. | [optional] 
 **webhook_id** | **int**| WebHook id | [optional] 

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

# **webhookhistory_id_get**
> WebHookHistory webhookhistory_id_get(id)

Get a webhook history item by id

Webhook history items are stored in the database and can be accessed via the API. They are preserved for 15 in both the live and sandbox environments.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.web_hook_history import WebHookHistory
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
    api_instance = invoicetronic_sdk.WebhookApi(api_client)
    id = 56 # int | Item id

    try:
        # Get a webhook history item by id
        api_response = api_instance.webhookhistory_id_get(id)
        print("The response of WebhookApi->webhookhistory_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhookhistory_id_get: %s\n" % e)
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

