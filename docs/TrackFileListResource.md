# TrackFileListResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track_file_ids** | **List[int]** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 

## Example

```python
from lidarr.models.track_file_list_resource import TrackFileListResource

# TODO update the JSON string below
json = "{}"
# create an instance of TrackFileListResource from a JSON string
track_file_list_resource_instance = TrackFileListResource.from_json(json)
# print the JSON string representation of the object
print TrackFileListResource.to_json()

# convert the object into a dict
track_file_list_resource_dict = track_file_list_resource_instance.to_dict()
# create an instance of TrackFileListResource from a dict
track_file_list_resource_form_dict = track_file_list_resource.from_dict(track_file_list_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


