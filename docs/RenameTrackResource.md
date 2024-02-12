# RenameTrackResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**artist_id** | **int** |  | [optional] 
**album_id** | **int** |  | [optional] 
**track_numbers** | **List[int]** |  | [optional] 
**track_file_id** | **int** |  | [optional] 
**existing_path** | **str** |  | [optional] 
**new_path** | **str** |  | [optional] 

## Example

```python
from lidarr.models.rename_track_resource import RenameTrackResource

# TODO update the JSON string below
json = "{}"
# create an instance of RenameTrackResource from a JSON string
rename_track_resource_instance = RenameTrackResource.from_json(json)
# print the JSON string representation of the object
print RenameTrackResource.to_json()

# convert the object into a dict
rename_track_resource_dict = rename_track_resource_instance.to_dict()
# create an instance of RenameTrackResource from a dict
rename_track_resource_form_dict = rename_track_resource.from_dict(rename_track_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


