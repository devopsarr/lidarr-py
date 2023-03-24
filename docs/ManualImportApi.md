# lidarr.ManualImportApi

All URIs are relative to *http://localhost:8686*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_import**](ManualImportApi.md#create_manual_import) | **POST** /api/v1/manualimport | 
[**list_manual_import**](ManualImportApi.md#list_manual_import) | **GET** /api/v1/manualimport | 


# **create_manual_import**
> create_manual_import(manual_import_update_resource=manual_import_update_resource)



### Example

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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with lidarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lidarr.ManualImportApi(api_client)
    manual_import_update_resource = [lidarr.ManualImportUpdateResource()] # List[ManualImportUpdateResource] |  (optional)

    try:
        api_instance.create_manual_import(manual_import_update_resource=manual_import_update_resource)
    except Exception as e:
        print("Exception when calling ManualImportApi->create_manual_import: %s\n" % e)
```

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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with lidarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lidarr.ManualImportApi(api_client)
    manual_import_update_resource = [lidarr.ManualImportUpdateResource()] # List[ManualImportUpdateResource] |  (optional)

    try:
        api_instance.create_manual_import(manual_import_update_resource=manual_import_update_resource)
    except Exception as e:
        print("Exception when calling ManualImportApi->create_manual_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_import_update_resource** | [**List[ManualImportUpdateResource]**](ManualImportUpdateResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_manual_import**
> List[ManualImportResource] list_manual_import(folder=folder, download_id=download_id, artist_id=artist_id, filter_existing_files=filter_existing_files, replace_existing_files=replace_existing_files)



### Example

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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

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

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

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

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

