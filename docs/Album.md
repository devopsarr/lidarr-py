# Album


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**artist_metadata_id** | **int** |  | [optional] 
**foreign_album_id** | **str** |  | [optional] 
**old_foreign_album_ids** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**release_date** | **datetime** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**album_type** | **str** |  | [optional] 
**secondary_types** | [**List[SecondaryAlbumType]**](SecondaryAlbumType.md) |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**clean_title** | **str** |  | [optional] 
**profile_id** | **int** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**any_release_ok** | **bool** |  | [optional] 
**last_info_sync** | **datetime** |  | [optional] 
**added** | **datetime** |  | [optional] 
**add_options** | [**AddAlbumOptions**](AddAlbumOptions.md) |  | [optional] 
**artist_metadata** | [**ArtistMetadataLazyLoaded**](ArtistMetadataLazyLoaded.md) |  | [optional] 
**album_releases** | [**AlbumReleaseListLazyLoaded**](AlbumReleaseListLazyLoaded.md) |  | [optional] 
**artist** | [**ArtistLazyLoaded**](ArtistLazyLoaded.md) |  | [optional] 

## Example

```python
from lidarr.models.album import Album

# TODO update the JSON string below
json = "{}"
# create an instance of Album from a JSON string
album_instance = Album.from_json(json)
# print the JSON string representation of the object
print Album.to_json()

# convert the object into a dict
album_dict = album_instance.to_dict()
# create an instance of Album from a dict
album_form_dict = album.from_dict(album_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


