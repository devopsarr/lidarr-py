# MonitoringOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor** | [**MonitorTypes**](MonitorTypes.md) |  | [optional] 
**albums_to_monitor** | **List[str]** |  | [optional] 
**monitored** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.monitoring_options import MonitoringOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoringOptions from a JSON string
monitoring_options_instance = MonitoringOptions.from_json(json)
# print the JSON string representation of the object
print MonitoringOptions.to_json()

# convert the object into a dict
monitoring_options_dict = monitoring_options_instance.to_dict()
# create an instance of MonitoringOptions from a dict
monitoring_options_form_dict = monitoring_options.from_dict(monitoring_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


