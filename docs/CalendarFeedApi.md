# lidarr.CalendarFeedApi

All URIs are relative to *http://localhost:8686*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feed_v1_calendar_lidarr_ics**](CalendarFeedApi.md#get_feed_v1_calendar_lidarr_ics) | **GET** /feed/v1/calendar/lidarr.ics | 


# **get_feed_v1_calendar_lidarr_ics**
> get_feed_v1_calendar_lidarr_ics(past_days=past_days, future_days=future_days, tag_list=tag_list, unmonitored=unmonitored)



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
    api_instance = lidarr.CalendarFeedApi(api_client)
    past_days = 7 # int |  (optional) (default to 7)
    future_days = 28 # int |  (optional) (default to 28)
    tag_list = '' # str |  (optional) (default to '')
    unmonitored = False # bool |  (optional) (default to False)

    try:
        api_instance.get_feed_v1_calendar_lidarr_ics(past_days=past_days, future_days=future_days, tag_list=tag_list, unmonitored=unmonitored)
    except Exception as e:
        print("Exception when calling CalendarFeedApi->get_feed_v1_calendar_lidarr_ics: %s\n" % e)
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
    api_instance = lidarr.CalendarFeedApi(api_client)
    past_days = 7 # int |  (optional) (default to 7)
    future_days = 28 # int |  (optional) (default to 28)
    tag_list = '' # str |  (optional) (default to '')
    unmonitored = False # bool |  (optional) (default to False)

    try:
        api_instance.get_feed_v1_calendar_lidarr_ics(past_days=past_days, future_days=future_days, tag_list=tag_list, unmonitored=unmonitored)
    except Exception as e:
        print("Exception when calling CalendarFeedApi->get_feed_v1_calendar_lidarr_ics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **past_days** | **int**|  | [optional] [default to 7]
 **future_days** | **int**|  | [optional] [default to 28]
 **tag_list** | **str**|  | [optional] [default to &#39;&#39;]
 **unmonitored** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

