# AlbumStudioResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist** | [**List[AlbumStudioArtistResource]**](AlbumStudioArtistResource.md) |  | [optional] 
**monitoring_options** | [**MonitoringOptions**](MonitoringOptions.md) |  | [optional] 
**monitor_new_items** | [**NewItemMonitorTypes**](NewItemMonitorTypes.md) |  | [optional] 

## Example

```python
from lidarr.models.album_studio_resource import AlbumStudioResource

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumStudioResource from a JSON string
album_studio_resource_instance = AlbumStudioResource.from_json(json)
# print the JSON string representation of the object
print(AlbumStudioResource.to_json())

# convert the object into a dict
album_studio_resource_dict = album_studio_resource_instance.to_dict()
# create an instance of AlbumStudioResource from a dict
album_studio_resource_from_dict = AlbumStudioResource.from_dict(album_studio_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


