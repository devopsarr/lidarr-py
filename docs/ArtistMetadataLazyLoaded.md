# ArtistMetadataLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ArtistMetadata**](ArtistMetadata.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.artist_metadata_lazy_loaded import ArtistMetadataLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistMetadataLazyLoaded from a JSON string
artist_metadata_lazy_loaded_instance = ArtistMetadataLazyLoaded.from_json(json)
# print the JSON string representation of the object
print ArtistMetadataLazyLoaded.to_json()

# convert the object into a dict
artist_metadata_lazy_loaded_dict = artist_metadata_lazy_loaded_instance.to_dict()
# create an instance of ArtistMetadataLazyLoaded from a dict
artist_metadata_lazy_loaded_form_dict = artist_metadata_lazy_loaded.from_dict(artist_metadata_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


