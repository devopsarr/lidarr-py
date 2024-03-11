# ProfilePrimaryAlbumTypeItemResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**album_type** | [**PrimaryAlbumType**](PrimaryAlbumType.md) |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.profile_primary_album_type_item_resource import ProfilePrimaryAlbumTypeItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePrimaryAlbumTypeItemResource from a JSON string
profile_primary_album_type_item_resource_instance = ProfilePrimaryAlbumTypeItemResource.from_json(json)
# print the JSON string representation of the object
print(ProfilePrimaryAlbumTypeItemResource.to_json())

# convert the object into a dict
profile_primary_album_type_item_resource_dict = profile_primary_album_type_item_resource_instance.to_dict()
# create an instance of ProfilePrimaryAlbumTypeItemResource from a dict
profile_primary_album_type_item_resource_form_dict = profile_primary_album_type_item_resource.from_dict(profile_primary_album_type_item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


