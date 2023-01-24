# Track


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**foreign_track_id** | **str** |  | [optional] 
**old_foreign_track_ids** | **List[str]** |  | [optional] 
**foreign_recording_id** | **str** |  | [optional] 
**old_foreign_recording_ids** | **List[str]** |  | [optional] 
**album_release_id** | **int** |  | [optional] 
**artist_metadata_id** | **int** |  | [optional] 
**track_number** | **str** |  | [optional] 
**absolute_track_number** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**explicit** | **bool** |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**medium_number** | **int** |  | [optional] 
**track_file_id** | **int** |  | [optional] 
**has_file** | **bool** |  | [optional] [readonly] 
**album_release** | [**AlbumReleaseLazyLoaded**](AlbumReleaseLazyLoaded.md) |  | [optional] 
**artist_metadata** | [**ArtistMetadataLazyLoaded**](ArtistMetadataLazyLoaded.md) |  | [optional] 
**track_file** | [**TrackFileLazyLoaded**](TrackFileLazyLoaded.md) |  | [optional] 
**artist** | [**ArtistLazyLoaded**](ArtistLazyLoaded.md) |  | [optional] 
**album_id** | **int** |  | [optional] 
**album** | [**Album**](Album.md) |  | [optional] 

## Example

```python
from lidarr.models.track import Track

# TODO update the JSON string below
json = "{}"
# create an instance of Track from a JSON string
track_instance = Track.from_json(json)
# print the JSON string representation of the object
print Track.to_json()

# convert the object into a dict
track_dict = track_instance.to_dict()
# create an instance of Track from a dict
track_form_dict = track.from_dict(track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


