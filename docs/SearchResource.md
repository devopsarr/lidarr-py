# SearchResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**foreign_id** | **str** |  | [optional] 
**artist** | [**ArtistResource**](ArtistResource.md) |  | [optional] 
**album** | [**AlbumResource**](AlbumResource.md) |  | [optional] 

## Example

```python
from lidarr.models.search_resource import SearchResource

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResource from a JSON string
search_resource_instance = SearchResource.from_json(json)
# print the JSON string representation of the object
print(SearchResource.to_json())

# convert the object into a dict
search_resource_dict = search_resource_instance.to_dict()
# create an instance of SearchResource from a dict
search_resource_from_dict = SearchResource.from_dict(search_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


