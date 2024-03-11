# IsoCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**two_letter_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from lidarr.models.iso_country import IsoCountry

# TODO update the JSON string below
json = "{}"
# create an instance of IsoCountry from a JSON string
iso_country_instance = IsoCountry.from_json(json)
# print the JSON string representation of the object
print(IsoCountry.to_json())

# convert the object into a dict
iso_country_dict = iso_country_instance.to_dict()
# create an instance of IsoCountry from a dict
iso_country_form_dict = iso_country.from_dict(iso_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


