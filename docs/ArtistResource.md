# ArtistResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**artist_metadata_id** | **int** |  | [optional] 
**status** | [**ArtistStatusType**](ArtistStatusType.md) |  | [optional] 
**ended** | **bool** |  | [optional] [readonly] 
**artist_name** | **str** |  | [optional] 
**foreign_artist_id** | **str** |  | [optional] 
**mb_id** | **str** |  | [optional] 
**tadb_id** | **int** |  | [optional] 
**discogs_id** | **int** |  | [optional] 
**all_music_id** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**artist_type** | **str** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**next_album** | [**Album**](Album.md) |  | [optional] 
**last_album** | [**Album**](Album.md) |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**members** | [**List[Member]**](Member.md) |  | [optional] 
**remote_poster** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**metadata_profile_id** | **int** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**monitor_new_items** | [**NewItemMonitorTypes**](NewItemMonitorTypes.md) |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**folder** | **str** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**clean_name** | **str** |  | [optional] 
**sort_name** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**added** | **datetime** |  | [optional] 
**add_options** | [**AddArtistOptions**](AddArtistOptions.md) |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**statistics** | [**ArtistStatisticsResource**](ArtistStatisticsResource.md) |  | [optional] 

## Example

```python
from lidarr.models.artist_resource import ArtistResource

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistResource from a JSON string
artist_resource_instance = ArtistResource.from_json(json)
# print the JSON string representation of the object
print ArtistResource.to_json()

# convert the object into a dict
artist_resource_dict = artist_resource_instance.to_dict()
# create an instance of ArtistResource from a dict
artist_resource_form_dict = artist_resource.from_dict(artist_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


