# ArtistMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**foreign_artist_id** | **str** |  | [optional] 
**old_foreign_artist_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**overview** | **str** |  | [optional] 
**disambiguation** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**status** | [**ArtistStatusType**](ArtistStatusType.md) |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**links** | [**List[Links]**](Links.md) |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**members** | [**List[Member]**](Member.md) |  | [optional] 

## Example

```python
from lidarr.models.artist_metadata import ArtistMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistMetadata from a JSON string
artist_metadata_instance = ArtistMetadata.from_json(json)
# print the JSON string representation of the object
print ArtistMetadata.to_json()

# convert the object into a dict
artist_metadata_dict = artist_metadata_instance.to_dict()
# create an instance of ArtistMetadata from a dict
artist_metadata_form_dict = artist_metadata.from_dict(artist_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


