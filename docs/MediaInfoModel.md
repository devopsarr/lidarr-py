# MediaInfoModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_format** | **str** |  | [optional] 
**audio_bitrate** | **int** |  | [optional] 
**audio_channels** | **int** |  | [optional] 
**audio_bits** | **int** |  | [optional] 
**audio_sample_rate** | **int** |  | [optional] 

## Example

```python
from lidarr.models.media_info_model import MediaInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of MediaInfoModel from a JSON string
media_info_model_instance = MediaInfoModel.from_json(json)
# print the JSON string representation of the object
print MediaInfoModel.to_json()

# convert the object into a dict
media_info_model_dict = media_info_model_instance.to_dict()
# create an instance of MediaInfoModel from a dict
media_info_model_form_dict = media_info_model.from_dict(media_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


