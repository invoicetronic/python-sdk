# invoicetronic_sdk.HealthApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get**](HealthApi.md#health_get) | **GET** /health | Health check


# **health_get**
> health_get()

Health check

Returns the health status of the API and its dependencies. No authentication required. Rate limited to 12 requests per minute.

### Example


```python
import invoicetronic_sdk
from invoicetronic_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.invoicetronic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = invoicetronic_sdk.Configuration(
    host = "https://api.invoicetronic.com"
)


# Enter a context with an instance of the API client
with invoicetronic_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoicetronic_sdk.HealthApi(api_client)

    try:
        # Health check
        api_instance.health_get()
    except Exception as e:
        print("Exception when calling HealthApi->health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

