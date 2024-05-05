# TagDifference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**old_value** | **str** |  | [optional] 
**new_value** | **str** |  | [optional] 

## Example

```python
from lidarr.models.tag_difference import TagDifference

# TODO update the JSON string below
json = "{}"
# create an instance of TagDifference from a JSON string
tag_difference_instance = TagDifference.from_json(json)
# print the JSON string representation of the object
print(TagDifference.to_json())

# convert the object into a dict
tag_difference_dict = tag_difference_instance.to_dict()
# create an instance of TagDifference from a dict
tag_difference_from_dict = TagDifference.from_dict(tag_difference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


