# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.1.7.4030
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class NamingConfigResource(BaseModel):
    """
    NamingConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    rename_tracks: Optional[StrictBool] = Field(default=None, alias="renameTracks")
    replace_illegal_characters: Optional[StrictBool] = Field(default=None, alias="replaceIllegalCharacters")
    colon_replacement_format: Optional[StrictInt] = Field(default=None, alias="colonReplacementFormat")
    standard_track_format: Optional[StrictStr] = Field(default=None, alias="standardTrackFormat")
    multi_disc_track_format: Optional[StrictStr] = Field(default=None, alias="multiDiscTrackFormat")
    artist_folder_format: Optional[StrictStr] = Field(default=None, alias="artistFolderFormat")
    include_artist_name: Optional[StrictBool] = Field(default=None, alias="includeArtistName")
    include_album_title: Optional[StrictBool] = Field(default=None, alias="includeAlbumTitle")
    include_quality: Optional[StrictBool] = Field(default=None, alias="includeQuality")
    replace_spaces: Optional[StrictBool] = Field(default=None, alias="replaceSpaces")
    separator: Optional[StrictStr] = None
    number_style: Optional[StrictStr] = Field(default=None, alias="numberStyle")
    __properties: ClassVar[List[str]] = ["id", "renameTracks", "replaceIllegalCharacters", "colonReplacementFormat", "standardTrackFormat", "multiDiscTrackFormat", "artistFolderFormat", "includeArtistName", "includeAlbumTitle", "includeQuality", "replaceSpaces", "separator", "numberStyle"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NamingConfigResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if standard_track_format (nullable) is None
        # and model_fields_set contains the field
        if self.standard_track_format is None and "standard_track_format" in self.model_fields_set:
            _dict['standardTrackFormat'] = None

        # set to None if multi_disc_track_format (nullable) is None
        # and model_fields_set contains the field
        if self.multi_disc_track_format is None and "multi_disc_track_format" in self.model_fields_set:
            _dict['multiDiscTrackFormat'] = None

        # set to None if artist_folder_format (nullable) is None
        # and model_fields_set contains the field
        if self.artist_folder_format is None and "artist_folder_format" in self.model_fields_set:
            _dict['artistFolderFormat'] = None

        # set to None if separator (nullable) is None
        # and model_fields_set contains the field
        if self.separator is None and "separator" in self.model_fields_set:
            _dict['separator'] = None

        # set to None if number_style (nullable) is None
        # and model_fields_set contains the field
        if self.number_style is None and "number_style" in self.model_fields_set:
            _dict['numberStyle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NamingConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "renameTracks": obj.get("renameTracks"),
            "replaceIllegalCharacters": obj.get("replaceIllegalCharacters"),
            "colonReplacementFormat": obj.get("colonReplacementFormat"),
            "standardTrackFormat": obj.get("standardTrackFormat"),
            "multiDiscTrackFormat": obj.get("multiDiscTrackFormat"),
            "artistFolderFormat": obj.get("artistFolderFormat"),
            "includeArtistName": obj.get("includeArtistName"),
            "includeAlbumTitle": obj.get("includeAlbumTitle"),
            "includeQuality": obj.get("includeQuality"),
            "replaceSpaces": obj.get("replaceSpaces"),
            "separator": obj.get("separator"),
            "numberStyle": obj.get("numberStyle")
        })
        return _obj


