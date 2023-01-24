# MetadataProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**primary_album_types** | [**List[ProfilePrimaryAlbumTypeItem]**](ProfilePrimaryAlbumTypeItem.md) |  | [optional] 
**secondary_album_types** | [**List[ProfileSecondaryAlbumTypeItem]**](ProfileSecondaryAlbumTypeItem.md) |  | [optional] 
**release_statuses** | [**List[ProfileReleaseStatusItem]**](ProfileReleaseStatusItem.md) |  | [optional] 

## Example

```python
from lidarr.models.metadata_profile import MetadataProfile

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataProfile from a JSON string
metadata_profile_instance = MetadataProfile.from_json(json)
# print the JSON string representation of the object
print MetadataProfile.to_json()

# convert the object into a dict
metadata_profile_dict = metadata_profile_instance.to_dict()
# create an instance of MetadataProfile from a dict
metadata_profile_form_dict = metadata_profile.from_dict(metadata_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


