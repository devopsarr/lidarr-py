# ParsedAlbumInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_title** | **str** |  | [optional] 
**album_title** | **str** |  | [optional] 
**artist_name** | **str** |  | [optional] 
**album_type** | **str** |  | [optional] 
**artist_title_info** | [**ArtistTitleInfo**](ArtistTitleInfo.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**release_date** | **str** |  | [optional] 
**discography** | **bool** |  | [optional] 
**discography_start** | **int** |  | [optional] 
**discography_end** | **int** |  | [optional] 
**release_group** | **str** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**release_version** | **str** |  | [optional] 

## Example

```python
from lidarr.models.parsed_album_info import ParsedAlbumInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParsedAlbumInfo from a JSON string
parsed_album_info_instance = ParsedAlbumInfo.from_json(json)
# print the JSON string representation of the object
print(ParsedAlbumInfo.to_json())

# convert the object into a dict
parsed_album_info_dict = parsed_album_info_instance.to_dict()
# create an instance of ParsedAlbumInfo from a dict
parsed_album_info_from_dict = ParsedAlbumInfo.from_dict(parsed_album_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


