# TrackListLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Track]**](Track.md) |  | [optional] [readonly] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.track_list_lazy_loaded import TrackListLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of TrackListLazyLoaded from a JSON string
track_list_lazy_loaded_instance = TrackListLazyLoaded.from_json(json)
# print the JSON string representation of the object
print TrackListLazyLoaded.to_json()

# convert the object into a dict
track_list_lazy_loaded_dict = track_list_lazy_loaded_instance.to_dict()
# create an instance of TrackListLazyLoaded from a dict
track_list_lazy_loaded_form_dict = track_list_lazy_loaded.from_dict(track_list_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


