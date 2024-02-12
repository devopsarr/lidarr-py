# RetagTrackResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**artist_id** | **int** |  | [optional] 
**album_id** | **int** |  | [optional] 
**track_numbers** | **List[int]** |  | [optional] 
**track_file_id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**changes** | [**List[TagDifference]**](TagDifference.md) |  | [optional] 

## Example

```python
from lidarr.models.retag_track_resource import RetagTrackResource

# TODO update the JSON string below
json = "{}"
# create an instance of RetagTrackResource from a JSON string
retag_track_resource_instance = RetagTrackResource.from_json(json)
# print the JSON string representation of the object
print RetagTrackResource.to_json()

# convert the object into a dict
retag_track_resource_dict = retag_track_resource_instance.to_dict()
# create an instance of RetagTrackResource from a dict
retag_track_resource_form_dict = retag_track_resource.from_dict(retag_track_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


