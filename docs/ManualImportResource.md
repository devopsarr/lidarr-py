# ManualImportResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**artist** | [**ArtistResource**](ArtistResource.md) |  | [optional] 
**album** | [**AlbumResource**](AlbumResource.md) |  | [optional] 
**album_release_id** | **int** |  | [optional] 
**tracks** | [**List[TrackResource]**](TrackResource.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**release_group** | **str** |  | [optional] 
**quality_weight** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 
**rejections** | [**List[Rejection]**](Rejection.md) |  | [optional] 
**audio_tags** | [**ParsedTrackInfo**](ParsedTrackInfo.md) |  | [optional] 
**additional_file** | **bool** |  | [optional] 
**replace_existing_files** | **bool** |  | [optional] 
**disable_release_switching** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.manual_import_resource import ManualImportResource

# TODO update the JSON string below
json = "{}"
# create an instance of ManualImportResource from a JSON string
manual_import_resource_instance = ManualImportResource.from_json(json)
# print the JSON string representation of the object
print ManualImportResource.to_json()

# convert the object into a dict
manual_import_resource_dict = manual_import_resource_instance.to_dict()
# create an instance of ManualImportResource from a dict
manual_import_resource_form_dict = manual_import_resource.from_dict(manual_import_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


