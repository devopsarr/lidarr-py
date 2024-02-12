# AlbumResourcePagingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[AlbumResource]**](AlbumResource.md) |  | [optional] 

## Example

```python
from lidarr.models.album_resource_paging_resource import AlbumResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumResourcePagingResource from a JSON string
album_resource_paging_resource_instance = AlbumResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print AlbumResourcePagingResource.to_json()

# convert the object into a dict
album_resource_paging_resource_dict = album_resource_paging_resource_instance.to_dict()
# create an instance of AlbumResourcePagingResource from a dict
album_resource_paging_resource_form_dict = album_resource_paging_resource.from_dict(album_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


