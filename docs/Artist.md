# Artist


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**artist_metadata_id** | **int** |  | [optional] 
**clean_name** | **str** |  | [optional] 
**sort_name** | **str** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**monitor_new_items** | [**NewItemMonitorTypes**](NewItemMonitorTypes.md) |  | [optional] 
**last_info_sync** | **datetime** |  | [optional] 
**path** | **str** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**added** | **datetime** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**metadata_profile_id** | **int** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**add_options** | [**AddArtistOptions**](AddArtistOptions.md) |  | [optional] 
**metadata** | [**ArtistMetadataLazyLoaded**](ArtistMetadataLazyLoaded.md) |  | [optional] 
**quality_profile** | [**QualityProfileLazyLoaded**](QualityProfileLazyLoaded.md) |  | [optional] 
**metadata_profile** | [**MetadataProfileLazyLoaded**](MetadataProfileLazyLoaded.md) |  | [optional] 
**albums** | [**AlbumListLazyLoaded**](AlbumListLazyLoaded.md) |  | [optional] 
**name** | **str** |  | [optional] 
**foreign_artist_id** | **str** |  | [optional] 

## Example

```python
from lidarr.models.artist import Artist

# TODO update the JSON string below
json = "{}"
# create an instance of Artist from a JSON string
artist_instance = Artist.from_json(json)
# print the JSON string representation of the object
print Artist.to_json()

# convert the object into a dict
artist_dict = artist_instance.to_dict()
# create an instance of Artist from a dict
artist_form_dict = artist.from_dict(artist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


