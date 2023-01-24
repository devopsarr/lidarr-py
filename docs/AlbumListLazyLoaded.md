# AlbumListLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Album]**](Album.md) |  | [optional] [readonly] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.album_list_lazy_loaded import AlbumListLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumListLazyLoaded from a JSON string
album_list_lazy_loaded_instance = AlbumListLazyLoaded.from_json(json)
# print the JSON string representation of the object
print AlbumListLazyLoaded.to_json()

# convert the object into a dict
album_list_lazy_loaded_dict = album_list_lazy_loaded_instance.to_dict()
# create an instance of AlbumListLazyLoaded from a dict
album_list_lazy_loaded_form_dict = album_list_lazy_loaded.from_dict(album_list_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


