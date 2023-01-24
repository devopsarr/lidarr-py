# AlbumStatisticsResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track_file_count** | **int** |  | [optional] 
**track_count** | **int** |  | [optional] 
**total_track_count** | **int** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 
**percent_of_tracks** | **float** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.album_statistics_resource import AlbumStatisticsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumStatisticsResource from a JSON string
album_statistics_resource_instance = AlbumStatisticsResource.from_json(json)
# print the JSON string representation of the object
print AlbumStatisticsResource.to_json()

# convert the object into a dict
album_statistics_resource_dict = album_statistics_resource_instance.to_dict()
# create an instance of AlbumStatisticsResource from a dict
album_statistics_resource_form_dict = album_statistics_resource.from_dict(album_statistics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


