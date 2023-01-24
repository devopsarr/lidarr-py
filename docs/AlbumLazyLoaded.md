# AlbumLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Album**](Album.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.album_lazy_loaded import AlbumLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumLazyLoaded from a JSON string
album_lazy_loaded_instance = AlbumLazyLoaded.from_json(json)
# print the JSON string representation of the object
print AlbumLazyLoaded.to_json()

# convert the object into a dict
album_lazy_loaded_dict = album_lazy_loaded_instance.to_dict()
# create an instance of AlbumLazyLoaded from a dict
album_lazy_loaded_form_dict = album_lazy_loaded.from_dict(album_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


