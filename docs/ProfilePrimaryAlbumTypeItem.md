# ProfilePrimaryAlbumTypeItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_album_type** | [**PrimaryAlbumType**](PrimaryAlbumType.md) |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.profile_primary_album_type_item import ProfilePrimaryAlbumTypeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePrimaryAlbumTypeItem from a JSON string
profile_primary_album_type_item_instance = ProfilePrimaryAlbumTypeItem.from_json(json)
# print the JSON string representation of the object
print ProfilePrimaryAlbumTypeItem.to_json()

# convert the object into a dict
profile_primary_album_type_item_dict = profile_primary_album_type_item_instance.to_dict()
# create an instance of ProfilePrimaryAlbumTypeItem from a dict
profile_primary_album_type_item_form_dict = profile_primary_album_type_item.from_dict(profile_primary_album_type_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


