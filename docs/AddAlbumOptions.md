# AddAlbumOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_type** | [**AlbumAddType**](AlbumAddType.md) |  | [optional] 
**search_for_new_album** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.add_album_options import AddAlbumOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AddAlbumOptions from a JSON string
add_album_options_instance = AddAlbumOptions.from_json(json)
# print the JSON string representation of the object
print(AddAlbumOptions.to_json())

# convert the object into a dict
add_album_options_dict = add_album_options_instance.to_dict()
# create an instance of AddAlbumOptions from a dict
add_album_options_form_dict = add_album_options.from_dict(add_album_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


