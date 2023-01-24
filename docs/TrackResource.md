# TrackResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**artist_id** | **int** |  | [optional] 
**foreign_track_id** | **str** |  | [optional] 
**foreign_recording_id** | **str** |  | [optional] 
**track_file_id** | **int** |  | [optional] 
**album_id** | **int** |  | [optional] 
**explicit** | **bool** |  | [optional] 
**absolute_track_number** | **int** |  | [optional] 
**track_number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**track_file** | [**TrackFileResource**](TrackFileResource.md) |  | [optional] 
**medium_number** | **int** |  | [optional] 
**has_file** | **bool** |  | [optional] 
**artist** | [**ArtistResource**](ArtistResource.md) |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**grabbed** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.track_resource import TrackResource

# TODO update the JSON string below
json = "{}"
# create an instance of TrackResource from a JSON string
track_resource_instance = TrackResource.from_json(json)
# print the JSON string representation of the object
print TrackResource.to_json()

# convert the object into a dict
track_resource_dict = track_resource_instance.to_dict()
# create an instance of TrackResource from a dict
track_resource_form_dict = track_resource.from_dict(track_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


