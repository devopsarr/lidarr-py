# MetadataProfileResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**primary_album_types** | [**List[ProfilePrimaryAlbumTypeItemResource]**](ProfilePrimaryAlbumTypeItemResource.md) |  | [optional] 
**secondary_album_types** | [**List[ProfileSecondaryAlbumTypeItemResource]**](ProfileSecondaryAlbumTypeItemResource.md) |  | [optional] 
**release_statuses** | [**List[ProfileReleaseStatusItemResource]**](ProfileReleaseStatusItemResource.md) |  | [optional] 

## Example

```python
from lidarr.models.metadata_profile_resource import MetadataProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataProfileResource from a JSON string
metadata_profile_resource_instance = MetadataProfileResource.from_json(json)
# print the JSON string representation of the object
print(MetadataProfileResource.to_json())

# convert the object into a dict
metadata_profile_resource_dict = metadata_profile_resource_instance.to_dict()
# create an instance of MetadataProfileResource from a dict
metadata_profile_resource_from_dict = MetadataProfileResource.from_dict(metadata_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


