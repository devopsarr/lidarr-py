# ArtistLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Artist**](Artist.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.artist_lazy_loaded import ArtistLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistLazyLoaded from a JSON string
artist_lazy_loaded_instance = ArtistLazyLoaded.from_json(json)
# print the JSON string representation of the object
print ArtistLazyLoaded.to_json()

# convert the object into a dict
artist_lazy_loaded_dict = artist_lazy_loaded_instance.to_dict()
# create an instance of ArtistLazyLoaded from a dict
artist_lazy_loaded_form_dict = artist_lazy_loaded.from_dict(artist_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


