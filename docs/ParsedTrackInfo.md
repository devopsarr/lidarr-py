# ParsedTrackInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**clean_title** | **str** |  | [optional] 
**artist_title** | **str** |  | [optional] 
**album_title** | **str** |  | [optional] 
**artist_title_info** | [**ArtistTitleInfo**](ArtistTitleInfo.md) |  | [optional] 
**artist_mbid** | **str** |  | [optional] 
**album_mbid** | **str** |  | [optional] 
**release_mbid** | **str** |  | [optional] 
**recording_mbid** | **str** |  | [optional] 
**track_mbid** | **str** |  | [optional] 
**disc_number** | **int** |  | [optional] 
**disc_count** | **int** |  | [optional] 
**country** | [**IsoCountry**](IsoCountry.md) |  | [optional] 
**year** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**catalog_number** | **str** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**duration** | **str** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**media_info** | [**MediaInfoModel**](MediaInfoModel.md) |  | [optional] 
**track_numbers** | **List[int]** |  | [optional] 
**release_group** | **str** |  | [optional] 
**release_hash** | **str** |  | [optional] 

## Example

```python
from lidarr.models.parsed_track_info import ParsedTrackInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParsedTrackInfo from a JSON string
parsed_track_info_instance = ParsedTrackInfo.from_json(json)
# print the JSON string representation of the object
print ParsedTrackInfo.to_json()

# convert the object into a dict
parsed_track_info_dict = parsed_track_info_instance.to_dict()
# create an instance of ParsedTrackInfo from a dict
parsed_track_info_form_dict = parsed_track_info.from_dict(parsed_track_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


