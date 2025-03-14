# lidarr.LocalizationApi

All URIs are relative to *http://localhost:8686*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_localization**](LocalizationApi.md#get_localization) | **GET** /api/v1/localization | 


# **get_localization**
> LocalizationResource get_localization()

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import lidarr
from lidarr.models.localization_resource import LocalizationResource
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
    api_instance = lidarr.LocalizationApi(api_client)

    try:
        api_response = api_instance.get_localization()
        print("The response of LocalizationApi->get_localization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalizationApi->get_localization: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LocalizationResource**](LocalizationResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

