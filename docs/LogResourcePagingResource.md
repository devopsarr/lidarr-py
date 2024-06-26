# LogResourcePagingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[LogResource]**](LogResource.md) |  | [optional] 

## Example

```python
from lidarr.models.log_resource_paging_resource import LogResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of LogResourcePagingResource from a JSON string
log_resource_paging_resource_instance = LogResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print(LogResourcePagingResource.to_json())

# convert the object into a dict
log_resource_paging_resource_dict = log_resource_paging_resource_instance.to_dict()
# create an instance of LogResourcePagingResource from a dict
log_resource_paging_resource_from_dict = LogResourcePagingResource.from_dict(log_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


