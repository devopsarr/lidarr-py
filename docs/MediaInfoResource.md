# MediaInfoResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**audio_channels** | **float** |  | [optional] 
**audio_bit_rate** | **str** |  | [optional] 
**audio_codec** | **str** |  | [optional] 
**audio_bits** | **str** |  | [optional] 
**audio_sample_rate** | **str** |  | [optional] 

## Example

```python
from lidarr.models.media_info_resource import MediaInfoResource

# TODO update the JSON string below
json = "{}"
# create an instance of MediaInfoResource from a JSON string
media_info_resource_instance = MediaInfoResource.from_json(json)
# print the JSON string representation of the object
print MediaInfoResource.to_json()

# convert the object into a dict
media_info_resource_dict = media_info_resource_instance.to_dict()
# create an instance of MediaInfoResource from a dict
media_info_resource_form_dict = media_info_resource.from_dict(media_info_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


