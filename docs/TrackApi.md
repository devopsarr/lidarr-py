# lidarr.TrackApi

All URIs are relative to *http://localhost:8686*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_track_by_id**](TrackApi.md#get_track_by_id) | **GET** /api/v1/track/{id} | 
[**list_track**](TrackApi.md#list_track) | **GET** /api/v1/track | 


# **get_track_by_id**
> TrackResource get_track_by_id(id)



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
    api_instance = lidarr.TrackApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_track_by_id(id)
        print("The response of TrackApi->get_track_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackApi->get_track_by_id: %s\n" % e)
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
    api_instance = lidarr.TrackApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_track_by_id(id)
        print("The response of TrackApi->get_track_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackApi->get_track_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TrackResource**](TrackResource.md)

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

# **list_track**
> List[TrackResource] list_track(artist_id=artist_id, album_id=album_id, album_release_id=album_release_id, track_ids=track_ids)



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
    api_instance = lidarr.TrackApi(api_client)
    artist_id = 56 # int |  (optional)
    album_id = 56 # int |  (optional)
    album_release_id = 56 # int |  (optional)
    track_ids = [56] # List[int] |  (optional)

    try:
        api_response = api_instance.list_track(artist_id=artist_id, album_id=album_id, album_release_id=album_release_id, track_ids=track_ids)
        print("The response of TrackApi->list_track:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackApi->list_track: %s\n" % e)
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
    api_instance = lidarr.TrackApi(api_client)
    artist_id = 56 # int |  (optional)
    album_id = 56 # int |  (optional)
    album_release_id = 56 # int |  (optional)
    track_ids = [56] # List[int] |  (optional)

    try:
        api_response = api_instance.list_track(artist_id=artist_id, album_id=album_id, album_release_id=album_release_id, track_ids=track_ids)
        print("The response of TrackApi->list_track:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackApi->list_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_id** | **int**|  | [optional] 
 **album_id** | **int**|  | [optional] 
 **album_release_id** | **int**|  | [optional] 
 **track_ids** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**List[TrackResource]**](TrackResource.md)

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

