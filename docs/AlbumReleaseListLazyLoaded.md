# AlbumReleaseListLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlbumRelease]**](AlbumRelease.md) |  | [optional] [readonly] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.album_release_list_lazy_loaded import AlbumReleaseListLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumReleaseListLazyLoaded from a JSON string
album_release_list_lazy_loaded_instance = AlbumReleaseListLazyLoaded.from_json(json)
# print the JSON string representation of the object
print AlbumReleaseListLazyLoaded.to_json()

# convert the object into a dict
album_release_list_lazy_loaded_dict = album_release_list_lazy_loaded_instance.to_dict()
# create an instance of AlbumReleaseListLazyLoaded from a dict
album_release_list_lazy_loaded_form_dict = album_release_list_lazy_loaded.from_dict(album_release_list_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


