# HealthResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**source** | **str** |  | [optional] 
**type** | [**HealthCheckResult**](HealthCheckResult.md) |  | [optional] 
**message** | **str** |  | [optional] 
**wiki_url** | **str** |  | [optional] 

## Example

```python
from lidarr.models.health_resource import HealthResource

# TODO update the JSON string below
json = "{}"
# create an instance of HealthResource from a JSON string
health_resource_instance = HealthResource.from_json(json)
# print the JSON string representation of the object
print(HealthResource.to_json())

# convert the object into a dict
health_resource_dict = health_resource_instance.to_dict()
# create an instance of HealthResource from a dict
health_resource_from_dict = HealthResource.from_dict(health_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


