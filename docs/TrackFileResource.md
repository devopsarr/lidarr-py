# TrackFileResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**artist_id** | **int** |  | [optional] 
**album_id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**date_added** | **datetime** |  | [optional] 
**scene_name** | **str** |  | [optional] 
**release_group** | **str** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**quality_weight** | **int** |  | [optional] 
**custom_formats** | [**List[CustomFormatResource]**](CustomFormatResource.md) |  | [optional] 
**custom_format_score** | **int** |  | [optional] 
**media_info** | [**MediaInfoResource**](MediaInfoResource.md) |  | [optional] 
**quality_cutoff_not_met** | **bool** |  | [optional] 
**audio_tags** | [**ParsedTrackInfo**](ParsedTrackInfo.md) |  | [optional] 

## Example

```python
from lidarr.models.track_file_resource import TrackFileResource

# TODO update the JSON string below
json = "{}"
# create an instance of TrackFileResource from a JSON string
track_file_resource_instance = TrackFileResource.from_json(json)
# print the JSON string representation of the object
print TrackFileResource.to_json()

# convert the object into a dict
track_file_resource_dict = track_file_resource_instance.to_dict()
# create an instance of TrackFileResource from a dict
track_file_resource_form_dict = track_file_resource.from_dict(track_file_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


