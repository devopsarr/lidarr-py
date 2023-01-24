# ProfileSecondaryAlbumTypeItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secondary_album_type** | [**SecondaryAlbumType**](SecondaryAlbumType.md) |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.profile_secondary_album_type_item import ProfileSecondaryAlbumTypeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSecondaryAlbumTypeItem from a JSON string
profile_secondary_album_type_item_instance = ProfileSecondaryAlbumTypeItem.from_json(json)
# print the JSON string representation of the object
print ProfileSecondaryAlbumTypeItem.to_json()

# convert the object into a dict
profile_secondary_album_type_item_dict = profile_secondary_album_type_item_instance.to_dict()
# create an instance of ProfileSecondaryAlbumTypeItem from a dict
profile_secondary_album_type_item_form_dict = profile_secondary_album_type_item.from_dict(profile_secondary_album_type_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


