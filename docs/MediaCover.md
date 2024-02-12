# MediaCover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**cover_type** | [**MediaCoverTypes**](MediaCoverTypes.md) |  | [optional] 
**extension** | **str** |  | [optional] [readonly] 
**remote_url** | **str** |  | [optional] 

## Example

```python
from lidarr.models.media_cover import MediaCover

# TODO update the JSON string below
json = "{}"
# create an instance of MediaCover from a JSON string
media_cover_instance = MediaCover.from_json(json)
# print the JSON string representation of the object
print MediaCover.to_json()

# convert the object into a dict
media_cover_dict = media_cover_instance.to_dict()
# create an instance of MediaCover from a dict
media_cover_form_dict = media_cover.from_dict(media_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


