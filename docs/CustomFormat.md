# CustomFormat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**include_custom_format_when_renaming** | **bool** |  | [optional] 
**specifications** | [**List[ICustomFormatSpecification]**](ICustomFormatSpecification.md) |  | [optional] 

## Example

```python
from lidarr.models.custom_format import CustomFormat

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormat from a JSON string
custom_format_instance = CustomFormat.from_json(json)
# print the JSON string representation of the object
print CustomFormat.to_json()

# convert the object into a dict
custom_format_dict = custom_format_instance.to_dict()
# create an instance of CustomFormat from a dict
custom_format_form_dict = custom_format.from_dict(custom_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


