# invoicetronic_sdk.StatusApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get**](StatusApi.md#status_get) | **GET** /status | Account status


# **status_get**
> Status status_get()

Account status

Retrieve the number of operations (invoices + validations) and signatures left on your account.

When `signature_left` is 0, you will receive a `403 Forbidden` response when trying to sign an invoice. Likewise, if `operation_left` is 0, you will receive a `403 Forbidden` response when storing or validating an invoice.

You can also check your account status from the [Dashboard](https://dashboard.invoicetronic.com), where you can purchase additional operations and/or signatures.

**Please note** that these values are not enforced if you are on the [Sandbox](https://invoicetronic.com/en/docs/sandbox/).

### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.status import Status
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
    api_instance = invoicetronic_sdk.StatusApi(api_client)

    try:
        # Account status
        api_response = api_instance.status_get()
        print("The response of StatusApi->status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

