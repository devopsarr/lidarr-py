# lidarr.ManualImportApi

All URIs are relative to *http://localhost:8686*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_manual_import**](ManualImportApi.md#list_manual_import) | **GET** /api/v1/manualimport | 
[**put_manual_import**](ManualImportApi.md#put_manual_import) | **PUT** /api/v1/manualimport | 


# **list_manual_import**
> List[ManualImportResource] list_manual_import(folder=folder, download_id=download_id, artist_id=artist_id, filter_existing_files=filter_existing_files, replace_existing_files=replace_existing_files)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
import lidarr
from lidarr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8686
# See configuration.py for a list of all supported configuration parameters.
configuration = lidarr.Configuration(
    host = "http://localhost:8686"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with lidarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lidarr.ManualImportApi(api_client)
    folder = 'folder_example' # str |  (optional)
    download_id = 'download_id_example' # str |  (optional)
    artist_id = 56 # int |  (optional)
    filter_existing_files = True # bool |  (optional) (default to True)
    replace_existing_files = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.list_manual_import(folder=folder, download_id=download_id, artist_id=artist_id, filter_existing_files=filter_existing_files, replace_existing_files=replace_existing_files)
        print("The response of ManualImportApi->list_manual_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualImportApi->list_manual_import: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
import lidarr
from lidarr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8686
# See configuration.py for a list of all supported configuration parameters.
configuration = lidarr.Configuration(
    host = "http://localhost:8686"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with lidarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lidarr.ManualImportApi(api_client)
    folder = 'folder_example' # str |  (optional)
    download_id = 'download_id_example' # str |  (optional)
    artist_id = 56 # int |  (optional)
    filter_existing_files = True # bool |  (optional) (default to True)
    replace_existing_files = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.list_manual_import(folder=folder, download_id=download_id, artist_id=artist_id, filter_existing_files=filter_existing_files, replace_existing_files=replace_existing_files)
        print("The response of ManualImportApi->list_manual_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualImportApi->list_manual_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**|  | [optional] 
 **download_id** | **str**|  | [optional] 
 **artist_id** | **int**|  | [optional] 
 **filter_existing_files** | **bool**|  | [optional] [default to True]
 **replace_existing_files** | **bool**|  | [optional] [default to True]

### Return type

[**List[ManualImportResource]**](ManualImportResource.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_manual_import**
> put_manual_import(manual_import_resource=manual_import_resource)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
import lidarr
from lidarr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8686
# See configuration.py for a list of all supported configuration parameters.
configuration = lidarr.Configuration(
    host = "http://localhost:8686"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with lidarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lidarr.ManualImportApi(api_client)
    manual_import_resource = [lidarr.ManualImportResource()] # List[ManualImportResource] |  (optional)

    try:
        api_instance.put_manual_import(manual_import_resource=manual_import_resource)
    except Exception as e:
        print("Exception when calling ManualImportApi->put_manual_import: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
import lidarr
from lidarr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8686
# See configuration.py for a list of all supported configuration parameters.
configuration = lidarr.Configuration(
    host = "http://localhost:8686"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with lidarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lidarr.ManualImportApi(api_client)
    manual_import_resource = [lidarr.ManualImportResource()] # List[ManualImportResource] |  (optional)

    try:
        api_instance.put_manual_import(manual_import_resource=manual_import_resource)
    except Exception as e:
        print("Exception when calling ManualImportApi->put_manual_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_import_resource** | [**List[ManualImportResource]**](ManualImportResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

