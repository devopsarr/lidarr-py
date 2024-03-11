# ArtistTitleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**title_without_year** | **str** |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from lidarr.models.artist_title_info import ArtistTitleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistTitleInfo from a JSON string
artist_title_info_instance = ArtistTitleInfo.from_json(json)
# print the JSON string representation of the object
print(ArtistTitleInfo.to_json())

# convert the object into a dict
artist_title_info_dict = artist_title_info_instance.to_dict()
# create an instance of ArtistTitleInfo from a dict
artist_title_info_form_dict = artist_title_info.from_dict(artist_title_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


