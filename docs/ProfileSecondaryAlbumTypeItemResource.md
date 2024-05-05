# ProfileSecondaryAlbumTypeItemResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**album_type** | [**SecondaryAlbumType**](SecondaryAlbumType.md) |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.profile_secondary_album_type_item_resource import ProfileSecondaryAlbumTypeItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSecondaryAlbumTypeItemResource from a JSON string
profile_secondary_album_type_item_resource_instance = ProfileSecondaryAlbumTypeItemResource.from_json(json)
# print the JSON string representation of the object
print(ProfileSecondaryAlbumTypeItemResource.to_json())

# convert the object into a dict
profile_secondary_album_type_item_resource_dict = profile_secondary_album_type_item_resource_instance.to_dict()
# create an instance of ProfileSecondaryAlbumTypeItemResource from a dict
profile_secondary_album_type_item_resource_from_dict = ProfileSecondaryAlbumTypeItemResource.from_dict(profile_secondary_album_type_item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


