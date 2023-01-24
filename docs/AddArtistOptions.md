# AddArtistOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor** | [**MonitorTypes**](MonitorTypes.md) |  | [optional] 
**albums_to_monitor** | **List[str]** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**search_for_missing_albums** | **bool** |  | [optional] 

## Example

```python
from lidarr.models.add_artist_options import AddArtistOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AddArtistOptions from a JSON string
add_artist_options_instance = AddArtistOptions.from_json(json)
# print the JSON string representation of the object
print AddArtistOptions.to_json()

# convert the object into a dict
add_artist_options_dict = add_artist_options_instance.to_dict()
# create an instance of AddArtistOptions from a dict
add_artist_options_form_dict = add_artist_options.from_dict(add_artist_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


