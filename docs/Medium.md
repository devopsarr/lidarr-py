# Medium


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**format** | **str** |  | [optional] 

## Example

```python
from lidarr.models.medium import Medium

# TODO update the JSON string below
json = "{}"
# create an instance of Medium from a JSON string
medium_instance = Medium.from_json(json)
# print the JSON string representation of the object
print Medium.to_json()

# convert the object into a dict
medium_dict = medium_instance.to_dict()
# create an instance of Medium from a dict
medium_form_dict = medium.from_dict(medium_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


