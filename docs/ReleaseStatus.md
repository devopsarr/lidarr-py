# ReleaseStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from lidarr.models.release_status import ReleaseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseStatus from a JSON string
release_status_instance = ReleaseStatus.from_json(json)
# print the JSON string representation of the object
print(ReleaseStatus.to_json())

# convert the object into a dict
release_status_dict = release_status_instance.to_dict()
# create an instance of ReleaseStatus from a dict
release_status_from_dict = ReleaseStatus.from_dict(release_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


