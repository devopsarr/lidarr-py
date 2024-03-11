# MetadataProviderConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**metadata_source** | **str** |  | [optional] 
**write_audio_tags** | [**WriteAudioTagsType**](WriteAudioTagsType.md) |  | [optional] 
**scrub_audio_tags** | **bool** |  | [optional] 
**embed_cover_art** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.metadata_provider_config_resource import MetadataProviderConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataProviderConfigResource from a JSON string
metadata_provider_config_resource_instance = MetadataProviderConfigResource.from_json(json)
# print the JSON string representation of the object
print(MetadataProviderConfigResource.to_json())

# convert the object into a dict
metadata_provider_config_resource_dict = metadata_provider_config_resource_instance.to_dict()
# create an instance of MetadataProviderConfigResource from a dict
metadata_provider_config_resource_form_dict = metadata_provider_config_resource.from_dict(metadata_provider_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


