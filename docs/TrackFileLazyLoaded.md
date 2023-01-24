# TrackFileLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**TrackFile**](TrackFile.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.track_file_lazy_loaded import TrackFileLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of TrackFileLazyLoaded from a JSON string
track_file_lazy_loaded_instance = TrackFileLazyLoaded.from_json(json)
# print the JSON string representation of the object
print TrackFileLazyLoaded.to_json()

# convert the object into a dict
track_file_lazy_loaded_dict = track_file_lazy_loaded_instance.to_dict()
# create an instance of TrackFileLazyLoaded from a dict
track_file_lazy_loaded_form_dict = track_file_lazy_loaded.from_dict(track_file_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


