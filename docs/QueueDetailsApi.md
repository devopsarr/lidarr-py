# lidarr.QueueDetailsApi

All URIs are relative to *http://localhost:8686*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_queue_details**](QueueDetailsApi.md#list_queue_details) | **GET** /api/v1/queue/details | 


# **list_queue_details**
> List[QueueResource] list_queue_details(artist_id=artist_id, album_ids=album_ids, include_artist=include_artist, include_album=include_album)



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
    api_instance = lidarr.QueueDetailsApi(api_client)
    artist_id = 56 # int |  (optional)
    album_ids = [56] # List[int] |  (optional)
    include_artist = False # bool |  (optional) (default to False)
    include_album = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.list_queue_details(artist_id=artist_id, album_ids=album_ids, include_artist=include_artist, include_album=include_album)
        print("The response of QueueDetailsApi->list_queue_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueDetailsApi->list_queue_details: %s\n" % e)
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
    api_instance = lidarr.QueueDetailsApi(api_client)
    artist_id = 56 # int |  (optional)
    album_ids = [56] # List[int] |  (optional)
    include_artist = False # bool |  (optional) (default to False)
    include_album = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.list_queue_details(artist_id=artist_id, album_ids=album_ids, include_artist=include_artist, include_album=include_album)
        print("The response of QueueDetailsApi->list_queue_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueDetailsApi->list_queue_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_id** | **int**|  | [optional] 
 **album_ids** | [**List[int]**](int.md)|  | [optional] 
 **include_artist** | **bool**|  | [optional] [default to False]
 **include_album** | **bool**|  | [optional] [default to True]

### Return type

[**List[QueueResource]**](QueueResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

