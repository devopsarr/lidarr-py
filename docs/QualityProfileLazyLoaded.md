# QualityProfileLazyLoaded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**QualityProfile**](QualityProfile.md) |  | [optional] 
**is_loaded** | **bool** |  | [optional] [readonly] 

## Example

```python
from lidarr.models.quality_profile_lazy_loaded import QualityProfileLazyLoaded

# TODO update the JSON string below
json = "{}"
# create an instance of QualityProfileLazyLoaded from a JSON string
quality_profile_lazy_loaded_instance = QualityProfileLazyLoaded.from_json(json)
# print the JSON string representation of the object
print QualityProfileLazyLoaded.to_json()

# convert the object into a dict
quality_profile_lazy_loaded_dict = quality_profile_lazy_loaded_instance.to_dict()
# create an instance of QualityProfileLazyLoaded from a dict
quality_profile_lazy_loaded_form_dict = quality_profile_lazy_loaded.from_dict(quality_profile_lazy_loaded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


