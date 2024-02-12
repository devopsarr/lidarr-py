# MediumResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medium_number** | **int** |  | [optional] 
**medium_name** | **str** |  | [optional] 
**medium_format** | **str** |  | [optional] 

## Example

```python
from lidarr.models.medium_resource import MediumResource

# TODO update the JSON string below
json = "{}"
# create an instance of MediumResource from a JSON string
medium_resource_instance = MediumResource.from_json(json)
# print the JSON string representation of the object
print MediumResource.to_json()

# convert the object into a dict
medium_resource_dict = medium_resource_instance.to_dict()
# create an instance of MediumResource from a dict
medium_resource_form_dict = medium_resource.from_dict(medium_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


