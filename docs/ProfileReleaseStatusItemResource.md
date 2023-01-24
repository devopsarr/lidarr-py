# ProfileReleaseStatusItemResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.profile_release_status_item_resource import ProfileReleaseStatusItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileReleaseStatusItemResource from a JSON string
profile_release_status_item_resource_instance = ProfileReleaseStatusItemResource.from_json(json)
# print the JSON string representation of the object
print ProfileReleaseStatusItemResource.to_json()

# convert the object into a dict
profile_release_status_item_resource_dict = profile_release_status_item_resource_instance.to_dict()
# create an instance of ProfileReleaseStatusItemResource from a dict
profile_release_status_item_resource_form_dict = profile_release_status_item_resource.from_dict(profile_release_status_item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


