# QualityProfileQualityItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**quality** | [**Quality**](Quality.md) |  | [optional] 
**items** | [**List[QualityProfileQualityItem]**](QualityProfileQualityItem.md) |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.quality_profile_quality_item import QualityProfileQualityItem

# TODO update the JSON string below
json = "{}"
# create an instance of QualityProfileQualityItem from a JSON string
quality_profile_quality_item_instance = QualityProfileQualityItem.from_json(json)
# print the JSON string representation of the object
print QualityProfileQualityItem.to_json()

# convert the object into a dict
quality_profile_quality_item_dict = quality_profile_quality_item_instance.to_dict()
# create an instance of QualityProfileQualityItem from a dict
quality_profile_quality_item_form_dict = quality_profile_quality_item.from_dict(quality_profile_quality_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


