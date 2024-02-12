# TagDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**delay_profile_ids** | **List[int]** |  | [optional] 
**import_list_ids** | **List[int]** |  | [optional] 
**notification_ids** | **List[int]** |  | [optional] 
**restriction_ids** | **List[int]** |  | [optional] 
**indexer_ids** | **List[int]** |  | [optional] 
**download_client_ids** | **List[int]** |  | [optional] 
**auto_tag_ids** | **List[int]** |  | [optional] 
**artist_ids** | **List[int]** |  | [optional] 

## Example

```python
from lidarr.models.tag_details_resource import TagDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of TagDetailsResource from a JSON string
tag_details_resource_instance = TagDetailsResource.from_json(json)
# print the JSON string representation of the object
print TagDetailsResource.to_json()

# convert the object into a dict
tag_details_resource_dict = tag_details_resource_instance.to_dict()
# create an instance of TagDetailsResource from a dict
tag_details_resource_form_dict = tag_details_resource.from_dict(tag_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


