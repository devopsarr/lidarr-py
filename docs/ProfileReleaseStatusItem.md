# ProfileReleaseStatusItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.profile_release_status_item import ProfileReleaseStatusItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileReleaseStatusItem from a JSON string
profile_release_status_item_instance = ProfileReleaseStatusItem.from_json(json)
# print the JSON string representation of the object
print ProfileReleaseStatusItem.to_json()

# convert the object into a dict
profile_release_status_item_dict = profile_release_status_item_instance.to_dict()
# create an instance of ProfileReleaseStatusItem from a dict
profile_release_status_item_form_dict = profile_release_status_item.from_dict(profile_release_status_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


