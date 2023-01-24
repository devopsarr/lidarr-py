# AlbumReleaseLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**AlbumRelease**](AlbumRelease.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.album_release_lazy_loaded import AlbumReleaseLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumReleaseLazyLoaded from a JSON string
album_release_lazy_loaded_instance = AlbumReleaseLazyLoaded.from_json(json)
# print the JSON string representation of the object
print AlbumReleaseLazyLoaded.to_json()

# convert the object into a dict
album_release_lazy_loaded_dict = album_release_lazy_loaded_instance.to_dict()
# create an instance of AlbumReleaseLazyLoaded from a dict
album_release_lazy_loaded_form_dict = album_release_lazy_loaded.from_dict(album_release_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


