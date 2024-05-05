# AlbumStudioArtistResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**albums** | [**List[AlbumResource]**](AlbumResource.md) |  | [optional] 

## Example

```python
from lidarr.models.album_studio_artist_resource import AlbumStudioArtistResource

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumStudioArtistResource from a JSON string
album_studio_artist_resource_instance = AlbumStudioArtistResource.from_json(json)
# print the JSON string representation of the object
print(AlbumStudioArtistResource.to_json())

# convert the object into a dict
album_studio_artist_resource_dict = album_studio_artist_resource_instance.to_dict()
# create an instance of AlbumStudioArtistResource from a dict
album_studio_artist_resource_from_dict = AlbumStudioArtistResource.from_dict(album_studio_artist_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


