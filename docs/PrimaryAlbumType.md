# PrimaryAlbumType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from lidarr.models.primary_album_type import PrimaryAlbumType

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryAlbumType from a JSON string
primary_album_type_instance = PrimaryAlbumType.from_json(json)
# print the JSON string representation of the object
print(PrimaryAlbumType.to_json())

# convert the object into a dict
primary_album_type_dict = primary_album_type_instance.to_dict()
# create an instance of PrimaryAlbumType from a dict
primary_album_type_form_dict = primary_album_type.from_dict(primary_album_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


