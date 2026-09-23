# invoicetronic_sdk.SubkeyApi

All URIs are relative to *https://api.invoicetronic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subkey_get**](SubkeyApi.md#subkey_get) | **GET** /subkey | List restricted keys
[**subkey_id_delete**](SubkeyApi.md#subkey_id_delete) | **DELETE** /subkey/{id} | Delete a restricted key
[**subkey_id_get**](SubkeyApi.md#subkey_id_get) | **GET** /subkey/{id} | Get a restricted key by id
[**subkey_id_roll_post**](SubkeyApi.md#subkey_id_roll_post) | **POST** /subkey/{id}/roll | Roll the secrets of a restricted key
[**subkey_post**](SubkeyApi.md#subkey_post) | **POST** /subkey | Add a restricted key
[**subkey_put**](SubkeyApi.md#subkey_put) | **PUT** /subkey | Update a restricted key


# **subkey_get**
> List[SubKey] subkey_get(page=page, page_size=page_size, company_id=company_id, active=active, q=q)

List restricted keys

Retrieve a paginated list of the restricted keys of the calling main key. Secrets are never included.

**Restricted keys** are API keys created under your main key, with the permissions and companies you choose. Use them to give each of your customers, integrations or collaborators only the access they need: a restricted key limited to one company sees only that company's invoices, updates, webhooks and events.

Only a main key can manage restricted keys: a restricted key calling these endpoints gets `403 Forbidden` with `code` = `subkey_not_allowed`.

**Onboarding a company in two calls.** Create the company with `POST /company`, then create a restricted key limited to it with `POST /subkey` and `company_ids` = `[<company id>]`. Hand the key to your customer: it can operate only on that company.

**Secrets are shown once.** `test_key` and `live_key` are returned only when a key is created or rolled, never by reads. Store them safely. If a secret is lost or exposed, roll the key with `POST /subkey/{id}/roll`: its id, permissions, companies and CORS origins stay the same. Pass `expires_in_hours` (up to 168) to keep the replaced secrets working while you migrate; without it they stop working at once.

**Permissions** are set per resource. `company`, `send`, `receive` and `webhook` accept `Read` or `Write`; `update`, `log`, `webhookhistory`, `export` and `status` accept only `Read`. A missing resource means no access. Each permission cannot exceed the one of your main key (`400`, `code` = `permission_exceeds_parent`). On creation, omitted or empty `permissions` copy those of your main key at that moment.

| Resource | `Read` | `Write` |
|---|---|---|
| `company` | list and read companies | also create, update and delete them |
| `send` | list and read outgoing invoices | also send and validate invoices |
| `receive` | list and read incoming invoices | also delete them |
| `webhook` | list and read webhooks | also create, update and delete them |
| `update`, `log`, `webhookhistory`, `export`, `status` | read | — |

**Companies.** Omitted or empty `company_ids` give access to all the companies of your account, including the ones created later. Every id must belong to your account (`400`, `code` = `company_not_found`). A restricted key limited to some companies cannot see the companies it creates: use your main key for onboarding.

**Limits.** An account can hold up to 1,000 restricted keys (`400`, `code` = `subkey_limit_reached`). Operations performed with restricted keys use the credits of your account.


### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.sub_key import SubKey
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
    api_instance = invoicetronic_sdk.SubkeyApi(api_client)
    page = 1 # int | Page number. (optional) (default to 1)
    page_size = 100 # int | Items per page. Cannot be greater than 200. (optional) (default to 100)
    company_id = 56 # int | Company id (optional)
    active = True # bool | Active keys only (true) or inactive only (false). (optional)
    q = 'q_example' # str | Human-readable label: free-text search. (optional)

    try:
        # List restricted keys
        api_response = api_instance.subkey_get(page=page, page_size=page_size, company_id=company_id, active=active, q=q)
        print("The response of SubkeyApi->subkey_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubkeyApi->subkey_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. | [optional] [default to 1]
 **page_size** | **int**| Items per page. Cannot be greater than 200. | [optional] [default to 100]
 **company_id** | **int**| Company id | [optional] 
 **active** | **bool**| Active keys only (true) or inactive only (false). | [optional] 
 **q** | **str**| Human-readable label: free-text search. | [optional] 

### Return type

[**List[SubKey]**](SubKey.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subkey_id_delete**
> SubKey subkey_id_delete(id)

Delete a restricted key

Delete a restricted key of the calling main key. It stops authenticating at once.

**Restricted keys** are API keys created under your main key, with the permissions and companies you choose. Use them to give each of your customers, integrations or collaborators only the access they need: a restricted key limited to one company sees only that company's invoices, updates, webhooks and events.

Only a main key can manage restricted keys: a restricted key calling these endpoints gets `403 Forbidden` with `code` = `subkey_not_allowed`.

**Onboarding a company in two calls.** Create the company with `POST /company`, then create a restricted key limited to it with `POST /subkey` and `company_ids` = `[<company id>]`. Hand the key to your customer: it can operate only on that company.

**Secrets are shown once.** `test_key` and `live_key` are returned only when a key is created or rolled, never by reads. Store them safely. If a secret is lost or exposed, roll the key with `POST /subkey/{id}/roll`: its id, permissions, companies and CORS origins stay the same. Pass `expires_in_hours` (up to 168) to keep the replaced secrets working while you migrate; without it they stop working at once.

**Permissions** are set per resource. `company`, `send`, `receive` and `webhook` accept `Read` or `Write`; `update`, `log`, `webhookhistory`, `export` and `status` accept only `Read`. A missing resource means no access. Each permission cannot exceed the one of your main key (`400`, `code` = `permission_exceeds_parent`). On creation, omitted or empty `permissions` copy those of your main key at that moment.

| Resource | `Read` | `Write` |
|---|---|---|
| `company` | list and read companies | also create, update and delete them |
| `send` | list and read outgoing invoices | also send and validate invoices |
| `receive` | list and read incoming invoices | also delete them |
| `webhook` | list and read webhooks | also create, update and delete them |
| `update`, `log`, `webhookhistory`, `export`, `status` | read | — |

**Companies.** Omitted or empty `company_ids` give access to all the companies of your account, including the ones created later. Every id must belong to your account (`400`, `code` = `company_not_found`). A restricted key limited to some companies cannot see the companies it creates: use your main key for onboarding.

**Limits.** An account can hold up to 1,000 restricted keys (`400`, `code` = `subkey_limit_reached`). Operations performed with restricted keys use the credits of your account.


### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.sub_key import SubKey
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
    api_instance = invoicetronic_sdk.SubkeyApi(api_client)
    id = 56 # int | Item id

    try:
        # Delete a restricted key
        api_response = api_instance.subkey_id_delete(id)
        print("The response of SubkeyApi->subkey_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubkeyApi->subkey_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**SubKey**](SubKey.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subkey_id_get**
> SubKey subkey_id_get(id)

Get a restricted key by id

Retrieve a restricted key of the calling main key. Secrets are never included.

**Restricted keys** are API keys created under your main key, with the permissions and companies you choose. Use them to give each of your customers, integrations or collaborators only the access they need: a restricted key limited to one company sees only that company's invoices, updates, webhooks and events.

Only a main key can manage restricted keys: a restricted key calling these endpoints gets `403 Forbidden` with `code` = `subkey_not_allowed`.

**Onboarding a company in two calls.** Create the company with `POST /company`, then create a restricted key limited to it with `POST /subkey` and `company_ids` = `[<company id>]`. Hand the key to your customer: it can operate only on that company.

**Secrets are shown once.** `test_key` and `live_key` are returned only when a key is created or rolled, never by reads. Store them safely. If a secret is lost or exposed, roll the key with `POST /subkey/{id}/roll`: its id, permissions, companies and CORS origins stay the same. Pass `expires_in_hours` (up to 168) to keep the replaced secrets working while you migrate; without it they stop working at once.

**Permissions** are set per resource. `company`, `send`, `receive` and `webhook` accept `Read` or `Write`; `update`, `log`, `webhookhistory`, `export` and `status` accept only `Read`. A missing resource means no access. Each permission cannot exceed the one of your main key (`400`, `code` = `permission_exceeds_parent`). On creation, omitted or empty `permissions` copy those of your main key at that moment.

| Resource | `Read` | `Write` |
|---|---|---|
| `company` | list and read companies | also create, update and delete them |
| `send` | list and read outgoing invoices | also send and validate invoices |
| `receive` | list and read incoming invoices | also delete them |
| `webhook` | list and read webhooks | also create, update and delete them |
| `update`, `log`, `webhookhistory`, `export`, `status` | read | — |

**Companies.** Omitted or empty `company_ids` give access to all the companies of your account, including the ones created later. Every id must belong to your account (`400`, `code` = `company_not_found`). A restricted key limited to some companies cannot see the companies it creates: use your main key for onboarding.

**Limits.** An account can hold up to 1,000 restricted keys (`400`, `code` = `subkey_limit_reached`). Operations performed with restricted keys use the credits of your account.


### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.sub_key import SubKey
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
    api_instance = invoicetronic_sdk.SubkeyApi(api_client)
    id = 56 # int | Item id

    try:
        # Get a restricted key by id
        api_response = api_instance.subkey_id_get(id)
        print("The response of SubkeyApi->subkey_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubkeyApi->subkey_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 

### Return type

[**SubKey**](SubKey.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subkey_id_roll_post**
> SubKeyWithSecrets subkey_id_roll_post(id, expires_in_hours=expires_in_hours)

Roll the secrets of a restricted key

Generate new `test_key` and `live_key` for a restricted key, keeping its id, permissions, companies and CORS origins. The replaced secrets stop working at once, or after `expires_in_hours` to migrate without downtime. The response carries the new secrets: store them safely.

**Restricted keys** are API keys created under your main key, with the permissions and companies you choose. Use them to give each of your customers, integrations or collaborators only the access they need: a restricted key limited to one company sees only that company's invoices, updates, webhooks and events.

Only a main key can manage restricted keys: a restricted key calling these endpoints gets `403 Forbidden` with `code` = `subkey_not_allowed`.

**Onboarding a company in two calls.** Create the company with `POST /company`, then create a restricted key limited to it with `POST /subkey` and `company_ids` = `[<company id>]`. Hand the key to your customer: it can operate only on that company.

**Secrets are shown once.** `test_key` and `live_key` are returned only when a key is created or rolled, never by reads. Store them safely. If a secret is lost or exposed, roll the key with `POST /subkey/{id}/roll`: its id, permissions, companies and CORS origins stay the same. Pass `expires_in_hours` (up to 168) to keep the replaced secrets working while you migrate; without it they stop working at once.

**Permissions** are set per resource. `company`, `send`, `receive` and `webhook` accept `Read` or `Write`; `update`, `log`, `webhookhistory`, `export` and `status` accept only `Read`. A missing resource means no access. Each permission cannot exceed the one of your main key (`400`, `code` = `permission_exceeds_parent`). On creation, omitted or empty `permissions` copy those of your main key at that moment.

| Resource | `Read` | `Write` |
|---|---|---|
| `company` | list and read companies | also create, update and delete them |
| `send` | list and read outgoing invoices | also send and validate invoices |
| `receive` | list and read incoming invoices | also delete them |
| `webhook` | list and read webhooks | also create, update and delete them |
| `update`, `log`, `webhookhistory`, `export`, `status` | read | — |

**Companies.** Omitted or empty `company_ids` give access to all the companies of your account, including the ones created later. Every id must belong to your account (`400`, `code` = `company_not_found`). A restricted key limited to some companies cannot see the companies it creates: use your main key for onboarding.

**Limits.** An account can hold up to 1,000 restricted keys (`400`, `code` = `subkey_limit_reached`). Operations performed with restricted keys use the credits of your account.


### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.sub_key_with_secrets import SubKeyWithSecrets
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
    api_instance = invoicetronic_sdk.SubkeyApi(api_client)
    id = 56 # int | Item id
    expires_in_hours = 56 # int | Hours the replaced secrets keep working, from 1 to 168. When omitted, they stop working at once. (optional)

    try:
        # Roll the secrets of a restricted key
        api_response = api_instance.subkey_id_roll_post(id, expires_in_hours=expires_in_hours)
        print("The response of SubkeyApi->subkey_id_roll_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubkeyApi->subkey_id_roll_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Item id | 
 **expires_in_hours** | **int**| Hours the replaced secrets keep working, from 1 to 168. When omitted, they stop working at once. | [optional] 

### Return type

[**SubKeyWithSecrets**](SubKeyWithSecrets.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subkey_post**
> SubKeyWithSecrets subkey_post(sub_key_request)

Add a restricted key

Create a restricted key under the calling main key. The response is the only one carrying `test_key` and `live_key`, together with the one of a roll: store them safely.

**Restricted keys** are API keys created under your main key, with the permissions and companies you choose. Use them to give each of your customers, integrations or collaborators only the access they need: a restricted key limited to one company sees only that company's invoices, updates, webhooks and events.

Only a main key can manage restricted keys: a restricted key calling these endpoints gets `403 Forbidden` with `code` = `subkey_not_allowed`.

**Onboarding a company in two calls.** Create the company with `POST /company`, then create a restricted key limited to it with `POST /subkey` and `company_ids` = `[<company id>]`. Hand the key to your customer: it can operate only on that company.

**Secrets are shown once.** `test_key` and `live_key` are returned only when a key is created or rolled, never by reads. Store them safely. If a secret is lost or exposed, roll the key with `POST /subkey/{id}/roll`: its id, permissions, companies and CORS origins stay the same. Pass `expires_in_hours` (up to 168) to keep the replaced secrets working while you migrate; without it they stop working at once.

**Permissions** are set per resource. `company`, `send`, `receive` and `webhook` accept `Read` or `Write`; `update`, `log`, `webhookhistory`, `export` and `status` accept only `Read`. A missing resource means no access. Each permission cannot exceed the one of your main key (`400`, `code` = `permission_exceeds_parent`). On creation, omitted or empty `permissions` copy those of your main key at that moment.

| Resource | `Read` | `Write` |
|---|---|---|
| `company` | list and read companies | also create, update and delete them |
| `send` | list and read outgoing invoices | also send and validate invoices |
| `receive` | list and read incoming invoices | also delete them |
| `webhook` | list and read webhooks | also create, update and delete them |
| `update`, `log`, `webhookhistory`, `export`, `status` | read | — |

**Companies.** Omitted or empty `company_ids` give access to all the companies of your account, including the ones created later. Every id must belong to your account (`400`, `code` = `company_not_found`). A restricted key limited to some companies cannot see the companies it creates: use your main key for onboarding.

**Limits.** An account can hold up to 1,000 restricted keys (`400`, `code` = `subkey_limit_reached`). Operations performed with restricted keys use the credits of your account.


### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.sub_key_request import SubKeyRequest
from invoicetronic_sdk.models.sub_key_with_secrets import SubKeyWithSecrets
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
    api_instance = invoicetronic_sdk.SubkeyApi(api_client)
    sub_key_request = invoicetronic_sdk.SubKeyRequest() # SubKeyRequest | 

    try:
        # Add a restricted key
        api_response = api_instance.subkey_post(sub_key_request)
        print("The response of SubkeyApi->subkey_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubkeyApi->subkey_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_key_request** | [**SubKeyRequest**](SubKeyRequest.md)|  | 

### Return type

[**SubKeyWithSecrets**](SubKeyWithSecrets.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subkey_put**
> SubKey subkey_put(sub_key_update)

Update a restricted key

Replace the description, active flag, permissions, companies and CORS origins of a restricted key. Omitted `permissions`, `company_ids` or `cors_origins` mean none. A stale `version` fails with `422`.

**Restricted keys** are API keys created under your main key, with the permissions and companies you choose. Use them to give each of your customers, integrations or collaborators only the access they need: a restricted key limited to one company sees only that company's invoices, updates, webhooks and events.

Only a main key can manage restricted keys: a restricted key calling these endpoints gets `403 Forbidden` with `code` = `subkey_not_allowed`.

**Onboarding a company in two calls.** Create the company with `POST /company`, then create a restricted key limited to it with `POST /subkey` and `company_ids` = `[<company id>]`. Hand the key to your customer: it can operate only on that company.

**Secrets are shown once.** `test_key` and `live_key` are returned only when a key is created or rolled, never by reads. Store them safely. If a secret is lost or exposed, roll the key with `POST /subkey/{id}/roll`: its id, permissions, companies and CORS origins stay the same. Pass `expires_in_hours` (up to 168) to keep the replaced secrets working while you migrate; without it they stop working at once.

**Permissions** are set per resource. `company`, `send`, `receive` and `webhook` accept `Read` or `Write`; `update`, `log`, `webhookhistory`, `export` and `status` accept only `Read`. A missing resource means no access. Each permission cannot exceed the one of your main key (`400`, `code` = `permission_exceeds_parent`). On creation, omitted or empty `permissions` copy those of your main key at that moment.

| Resource | `Read` | `Write` |
|---|---|---|
| `company` | list and read companies | also create, update and delete them |
| `send` | list and read outgoing invoices | also send and validate invoices |
| `receive` | list and read incoming invoices | also delete them |
| `webhook` | list and read webhooks | also create, update and delete them |
| `update`, `log`, `webhookhistory`, `export`, `status` | read | — |

**Companies.** Omitted or empty `company_ids` give access to all the companies of your account, including the ones created later. Every id must belong to your account (`400`, `code` = `company_not_found`). A restricted key limited to some companies cannot see the companies it creates: use your main key for onboarding.

**Limits.** An account can hold up to 1,000 restricted keys (`400`, `code` = `subkey_limit_reached`). Operations performed with restricted keys use the credits of your account.


### Example

* Basic Authentication (Basic):

```python
import invoicetronic_sdk
from invoicetronic_sdk.models.sub_key import SubKey
from invoicetronic_sdk.models.sub_key_update import SubKeyUpdate
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
    api_instance = invoicetronic_sdk.SubkeyApi(api_client)
    sub_key_update = invoicetronic_sdk.SubKeyUpdate() # SubKeyUpdate | 

    try:
        # Update a restricted key
        api_response = api_instance.subkey_put(sub_key_update)
        print("The response of SubkeyApi->subkey_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubkeyApi->subkey_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_key_update** | [**SubKeyUpdate**](SubKeyUpdate.md)|  | 

### Return type

[**SubKey**](SubKey.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

