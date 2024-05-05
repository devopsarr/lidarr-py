# SecondaryAlbumType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from lidarr.models.secondary_album_type import SecondaryAlbumType

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryAlbumType from a JSON string
secondary_album_type_instance = SecondaryAlbumType.from_json(json)
# print the JSON string representation of the object
print(SecondaryAlbumType.to_json())

# convert the object into a dict
secondary_album_type_dict = secondary_album_type_instance.to_dict()
# create an instance of SecondaryAlbumType from a dict
secondary_album_type_from_dict = SecondaryAlbumType.from_dict(secondary_album_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


