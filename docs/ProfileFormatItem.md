# ProfileFormatItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**CustomFormat**](CustomFormat.md) |  | [optional] 
**score** | **int** |  | [optional] 

## Example

```python
from lidarr.models.profile_format_item import ProfileFormatItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileFormatItem from a JSON string
profile_format_item_instance = ProfileFormatItem.from_json(json)
# print the JSON string representation of the object
print ProfileFormatItem.to_json()

# convert the object into a dict
profile_format_item_dict = profile_format_item_instance.to_dict()
# create an instance of ProfileFormatItem from a dict
profile_format_item_form_dict = profile_format_item.from_dict(profile_format_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


