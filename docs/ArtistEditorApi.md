# lidarr.ArtistEditorApi

All URIs are relative to *http://localhost:8686*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_artist_editor**](ArtistEditorApi.md#delete_artist_editor) | **DELETE** /api/v1/artist/editor | 
[**put_artist_editor**](ArtistEditorApi.md#put_artist_editor) | **PUT** /api/v1/artist/editor | 


# **delete_artist_editor**
> delete_artist_editor(artist_editor_resource=artist_editor_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import lidarr
from lidarr.models.artist_editor_resource import ArtistEditorResource
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
    api_instance = lidarr.ArtistEditorApi(api_client)
    artist_editor_resource = lidarr.ArtistEditorResource() # ArtistEditorResource |  (optional)

    try:
        api_instance.delete_artist_editor(artist_editor_resource=artist_editor_resource)
    except Exception as e:
        print("Exception when calling ArtistEditorApi->delete_artist_editor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_editor_resource** | [**ArtistEditorResource**](ArtistEditorResource.md)|  | [optional] 

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
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_artist_editor**
> put_artist_editor(artist_editor_resource=artist_editor_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import lidarr
from lidarr.models.artist_editor_resource import ArtistEditorResource
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
    api_instance = lidarr.ArtistEditorApi(api_client)
    artist_editor_resource = lidarr.ArtistEditorResource() # ArtistEditorResource |  (optional)

    try:
        api_instance.put_artist_editor(artist_editor_resource=artist_editor_resource)
    except Exception as e:
        print("Exception when calling ArtistEditorApi->put_artist_editor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_editor_resource** | [**ArtistEditorResource**](ArtistEditorResource.md)|  | [optional] 

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
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

