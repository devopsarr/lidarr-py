# NamingConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**rename_tracks** | **bool** |  | [optional] 
**replace_illegal_characters** | **bool** |  | [optional] 
**colon_replacement_format** | **int** |  | [optional] 
**standard_track_format** | **str** |  | [optional] 
**multi_disc_track_format** | **str** |  | [optional] 
**artist_folder_format** | **str** |  | [optional] 
**include_artist_name** | **bool** |  | [optional] 
**include_album_title** | **bool** |  | [optional] 
**include_quality** | **bool** |  | [optional] 
**replace_spaces** | **bool** |  | [optional] 
**separator** | **str** |  | [optional] 
**number_style** | **str** |  | [optional] 

## Example

```python
from lidarr.models.naming_config_resource import NamingConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of NamingConfigResource from a JSON string
naming_config_resource_instance = NamingConfigResource.from_json(json)
# print the JSON string representation of the object
print(NamingConfigResource.to_json())

# convert the object into a dict
naming_config_resource_dict = naming_config_resource_instance.to_dict()
# create an instance of NamingConfigResource from a dict
naming_config_resource_from_dict = NamingConfigResource.from_dict(naming_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


