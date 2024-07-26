# AlbumResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**artist_id** | **int** |  | [optional] 
**foreign_album_id** | **str** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**any_release_ok** | **bool** |  | [optional] 
**profile_id** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**album_type** | **str** |  | [optional] 
**secondary_types** | **List[str]** |  | [optional] 
**medium_count** | **int** |  | [optional] [readonly] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**release_date** | **datetime** |  | [optional] 
**releases** | [**List[AlbumReleaseResource]**](AlbumReleaseResource.md) |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**media** | [**List[MediumResource]**](MediumResource.md) |  | [optional] 
**artist** | [**ArtistResource**](ArtistResource.md) |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**statistics** | [**AlbumStatisticsResource**](AlbumStatisticsResource.md) |  | [optional] 
**add_options** | [**AddAlbumOptions**](AddAlbumOptions.md) |  | [optional] 
**remote_cover** | **str** |  | [optional] 

## Example

```python
from lidarr.models.album_resource import AlbumResource

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumResource from a JSON string
album_resource_instance = AlbumResource.from_json(json)
# print the JSON string representation of the object
print(AlbumResource.to_json())

# convert the object into a dict
album_resource_dict = album_resource_instance.to_dict()
# create an instance of AlbumResource from a dict
album_resource_from_dict = AlbumResource.from_dict(album_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


