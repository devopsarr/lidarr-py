# AlbumsMonitoredResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_ids** | **List[int]** |  | [optional] 
**monitored** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.albums_monitored_resource import AlbumsMonitoredResource

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsMonitoredResource from a JSON string
albums_monitored_resource_instance = AlbumsMonitoredResource.from_json(json)
# print the JSON string representation of the object
print AlbumsMonitoredResource.to_json()

# convert the object into a dict
albums_monitored_resource_dict = albums_monitored_resource_instance.to_dict()
# create an instance of AlbumsMonitoredResource from a dict
albums_monitored_resource_form_dict = albums_monitored_resource.from_dict(albums_monitored_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


