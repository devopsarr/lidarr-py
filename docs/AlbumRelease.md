# AlbumRelease


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**album_id** | **int** |  | [optional] 
**foreign_release_id** | **str** |  | [optional] 
**old_foreign_release_ids** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**label** | **List[str]** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**country** | **List[str]** |  | [optional] 
**release_date** | **datetime** |  | [optional] 
**media** | [**List[Medium]**](Medium.md) |  | [optional] 
**track_count** | **int** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**album** | [**AlbumLazyLoaded**](AlbumLazyLoaded.md) |  | [optional] 
**tracks** | [**TrackListLazyLoaded**](TrackListLazyLoaded.md) |  | [optional] 

## Example

```python
from lidarr.models.album_release import AlbumRelease

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumRelease from a JSON string
album_release_instance = AlbumRelease.from_json(json)
# print the JSON string representation of the object
print AlbumRelease.to_json()

# convert the object into a dict
album_release_dict = album_release_instance.to_dict()
# create an instance of AlbumRelease from a dict
album_release_form_dict = album_release.from_dict(album_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


