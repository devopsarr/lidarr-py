# StringInt32KeyValuePair


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from lidarr.models.string_int32_key_value_pair import StringInt32KeyValuePair

# TODO update the JSON string below
json = "{}"
# create an instance of StringInt32KeyValuePair from a JSON string
string_int32_key_value_pair_instance = StringInt32KeyValuePair.from_json(json)
# print the JSON string representation of the object
print StringInt32KeyValuePair.to_json()

# convert the object into a dict
string_int32_key_value_pair_dict = string_int32_key_value_pair_instance.to_dict()
# create an instance of StringInt32KeyValuePair from a dict
string_int32_key_value_pair_form_dict = string_int32_key_value_pair.from_dict(string_int32_key_value_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


