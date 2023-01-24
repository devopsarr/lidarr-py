# TrackFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**date_added** | **datetime** |  | [optional] 
**scene_name** | **str** |  | [optional] 
**release_group** | **str** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**media_info** | [**MediaInfoModel**](MediaInfoModel.md) |  | [optional] 
**album_id** | **int** |  | [optional] 
**tracks** | [**TrackListLazyLoaded**](TrackListLazyLoaded.md) |  | [optional] 
**artist** | [**ArtistLazyLoaded**](ArtistLazyLoaded.md) |  | [optional] 
**album** | [**AlbumLazyLoaded**](AlbumLazyLoaded.md) |  | [optional] 

## Example

```python
from lidarr.models.track_file import TrackFile

# TODO update the JSON string below
json = "{}"
# create an instance of TrackFile from a JSON string
track_file_instance = TrackFile.from_json(json)
# print the JSON string representation of the object
print TrackFile.to_json()

# convert the object into a dict
track_file_dict = track_file_instance.to_dict()
# create an instance of TrackFile from a dict
track_file_form_dict = track_file.from_dict(track_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


