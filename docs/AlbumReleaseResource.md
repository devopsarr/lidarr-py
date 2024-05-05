# AlbumReleaseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**album_id** | **int** |  | [optional] 
**foreign_release_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**track_count** | **int** |  | [optional] 
**media** | [**List[MediumResource]**](MediumResource.md) |  | [optional] 
**medium_count** | **int** |  | [optional] [readonly] 
**disambiguation** | **str** |  | [optional] 
**country** | **List[str]** |  | [optional] 
**label** | **List[str]** |  | [optional] 
**format** | **str** |  | [optional] 
**monitored** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.album_release_resource import AlbumReleaseResource

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumReleaseResource from a JSON string
album_release_resource_instance = AlbumReleaseResource.from_json(json)
# print the JSON string representation of the object
print(AlbumReleaseResource.to_json())

# convert the object into a dict
album_release_resource_dict = album_release_resource_instance.to_dict()
# create an instance of AlbumReleaseResource from a dict
album_release_resource_from_dict = AlbumReleaseResource.from_dict(album_release_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


