# ICustomFormatSpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | [optional] [readonly] 
**info_link** | **str** |  | [optional] [readonly] 
**implementation_name** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**negate** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.i_custom_format_specification import ICustomFormatSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ICustomFormatSpecification from a JSON string
i_custom_format_specification_instance = ICustomFormatSpecification.from_json(json)
# print the JSON string representation of the object
print ICustomFormatSpecification.to_json()

# convert the object into a dict
i_custom_format_specification_dict = i_custom_format_specification_instance.to_dict()
# create an instance of ICustomFormatSpecification from a dict
i_custom_format_specification_form_dict = i_custom_format_specification.from_dict(i_custom_format_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


