# invoicetronic_sdk.UpdateApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_get**](UpdateApi.md#update_get) | **GET** /update | List updates
[**update_id_get**](UpdateApi.md#update_id_get) | **GET** /update/{id} | Get an update by id


# **update_get**
> List[Update] update_get(company_id=company_id, identifier=identifier, prestatore=prestatore, unread=unread, send_id=send_id, state=state, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, page=page, page_size=page_size, sort=sort)

List updates

Retrieve a paginated list of updates. Results can be filtered by various criteria such as company, send item, SDI state, and date ranges.

**Updates** are status notifications from Italy's SDI (Sistema di Interscambio) about invoices you sent. Multiple updates can exist for the same send item as the invoice progresses through the SDI workflow.

The `state` field is the most important property and can have the following values:

| Value | Name | Description |
|-------|------|-------------|
| 2 | `Inviato` | Sent to the SDI. |
| 5 | `Consegnato` | Delivered to the recipient. |
| 6 | `NonConsegnato` | Not delivered to the recipient. Only relevant for public administration entities. |
| 7 | `Scartato` | Rejected by the SDI. |
| 8 | `AccettatoDalDestinatario` | Accepted by the recipient. Only relevant for public administration entities. |
| 9 | `RifiutatoDalDestinatario` | Rejected by the recipient. Only relevant for public administration entities. |
| 10 | `ImpossibilitaDiRecapito` | Available on the recipient's tax drawer, but it was not possible to deliver it to the recipient's reception system. |
| 11 | `DecorrenzaTermini` | A public administration entity has not responded for more than 15 days. The document is considered delivered. |
| 12 | `AttestazioneTrasmissioneFattura` | A public administration entity has received the document, but has not yet processed it. |

**Important:** Always monitor the state of your sent invoices. A state of `Inviato` only means the invoice has been submitted to SDI, not that it has been delivered. A state like `Scartato` indicates that the invoice was **not** successfully delivered and may require corrective action, such as fixing validation errors and resubmitting. In that case, `description` contains the reason for the rejection.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.update import Update
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
    api_instance = invoicetronic_sdk.UpdateApi(api_client)
    company_id = 56 # int | Company id (optional)
    identifier = 'identifier_example' # str | SDI identifier. (optional)
    prestatore = 'prestatore_example' # str | Vat number or fiscal code. (optional)
    unread = True # bool | Unread items only. (optional)
    send_id = 56 # int | Send item's id. (optional)
    state = 'state_example' # str | SDI state (optional)
    last_update_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    last_update_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    date_sent_from = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    date_sent_to = '2013-10-20T19:20:30+01:00' # datetime | UTC ISO 8601 (2024-11-29T12:34:56Z) (optional)
    page = 1 # int | Page number. (optional) (default to 1)
    page_size = 100 # int | Items per page. Cannot be greater than 200. (optional) (default to 100)
    sort = 'last_update' # str | Sort by field. Prefix with '-' for descending order. (optional) (default to 'last_update')

    try:
        # List updates
        api_response = api_instance.update_get(company_id=company_id, identifier=identifier, prestatore=prestatore, unread=unread, send_id=send_id, state=state, last_update_from=last_update_from, last_update_to=last_update_to, date_sent_from=date_sent_from, date_sent_to=date_sent_to, page=page, page_size=page_size, sort=sort)
        print("The response of UpdateApi->update_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateApi->update_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Company id | [optional] 
 **identifier** | **str**| SDI identifier. | [optional] 
 **prestatore** | **str**| Vat number or fiscal code. | [optional] 
 **unread** | **bool**| Unread items only. | [optional] 
 **send_id** | **int**| Send item&#39;s id. | [optional] 
 **state** | **str**| SDI state | [optional] 
 **last_update_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **last_update_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **date_sent_from** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **date_sent_to** | **datetime**| UTC ISO 8601 (2024-11-29T12:34:56Z) | [optional] 
 **page** | **int**| Page number. | [optional] [default to 1]
 **page_size** | **int**| Items per page. Cannot be greater than 200. | [optional] [default to 100]
 **sort** | **str**| Sort by field. Prefix with &#39;-&#39; for descending order. | [optional] [default to &#39;last_update&#39;]

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_id_get**
> Update update_id_get(id)

Get an update by id

Retrieve an update by its internal id.

**Updates** are status notifications from Italy's SDI (Sistema di Interscambio) about invoices you sent. Multiple updates can exist for the same send item as the invoice progresses through the SDI workflow.

The `state` field is the most important property and can have the following values:

| Value | Name | Description |
|-------|------|-------------|
| 2 | `Inviato` | Sent to the SDI. |
| 5 | `Consegnato` | Delivered to the recipient. |
| 6 | `NonConsegnato` | Not delivered to the recipient. Only relevant for public administration entities. |
| 7 | `Scartato` | Rejected by the SDI. |
| 8 | `AccettatoDalDestinatario` | Accepted by the recipient. Only relevant for public administration entities. |
| 9 | `RifiutatoDalDestinatario` | Rejected by the recipient. Only relevant for public administration entities. |
| 10 | `ImpossibilitaDiRecapito` | Available on the recipient's tax drawer, but it was not possible to deliver it to the recipient's reception system. |
| 11 | `DecorrenzaTermini` | A public administration entity has not responded for more than 15 days. The document is considered delivered. |
| 12 | `AttestazioneTrasmissioneFattura` | A public administration entity has received the document, but has not yet processed it. |

**Important:** Always monitor the state of your sent invoices. A state of `Inviato` only means the invoice has been submitted to SDI, not that it has been delivered. A state like `Scartato` indicates that the invoice was **not** successfully delivered and may require corrective action, such as fixing validation errors and resubmitting. In that case, `description` contains the reason for the rejection.

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.update import Update
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
    api_instance = invoicetronic_sdk.UpdateApi(api_client)
    id = 56 # int | Item id

    try:
        # Get an update by id
        api_response = api_instance.update_id_get(id)
        print("The response of UpdateApi->update_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateApi->update_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

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

