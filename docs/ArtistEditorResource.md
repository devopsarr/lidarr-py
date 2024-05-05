# ArtistEditorResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist_ids** | **List[int]** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**monitor_new_items** | [**NewItemMonitorTypes**](NewItemMonitorTypes.md) |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**metadata_profile_id** | **int** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 
**move_files** | **bool** |  | [optional] 
**delete_files** | **bool** |  | [optional] 
**add_import_list_exclusion** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.artist_editor_resource import ArtistEditorResource

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistEditorResource from a JSON string
artist_editor_resource_instance = ArtistEditorResource.from_json(json)
# print the JSON string representation of the object
print(ArtistEditorResource.to_json())

# convert the object into a dict
artist_editor_resource_dict = artist_editor_resource_instance.to_dict()
# create an instance of ArtistEditorResource from a dict
artist_editor_resource_from_dict = ArtistEditorResource.from_dict(artist_editor_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


