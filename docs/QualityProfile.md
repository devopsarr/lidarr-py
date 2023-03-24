# QualityProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**upgrade_allowed** | **bool** |  | [optional] 
**cutoff** | **int** |  | [optional] 
**min_format_score** | **int** |  | [optional] 
**cutoff_format_score** | **int** |  | [optional] 
**format_items** | [**List[ProfileFormatItem]**](ProfileFormatItem.md) |  | [optional] 
**items** | [**List[QualityProfileQualityItem]**](QualityProfileQualityItem.md) |  | [optional] 

## Example

```python
from lidarr.models.quality_profile import QualityProfile

# TODO update the JSON string below
json = "{}"
# create an instance of QualityProfile from a JSON string
quality_profile_instance = QualityProfile.from_json(json)
# print the JSON string representation of the object
print QualityProfile.to_json()

# convert the object into a dict
quality_profile_dict = quality_profile_instance.to_dict()
# create an instance of QualityProfile from a dict
quality_profile_form_dict = quality_profile.from_dict(quality_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


