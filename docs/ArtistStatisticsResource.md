# ArtistStatisticsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_count** | **int** |  | [optional] 
**track_file_count** | **int** |  | [optional] 
**track_count** | **int** |  | [optional] 
**total_track_count** | **int** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 
**percent_of_tracks** | **float** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.artist_statistics_resource import ArtistStatisticsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStatisticsResource from a JSON string
artist_statistics_resource_instance = ArtistStatisticsResource.from_json(json)
# print the JSON string representation of the object
print(ArtistStatisticsResource.to_json())

# convert the object into a dict
artist_statistics_resource_dict = artist_statistics_resource_instance.to_dict()
# create an instance of ArtistStatisticsResource from a dict
artist_statistics_resource_from_dict = ArtistStatisticsResource.from_dict(artist_statistics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


