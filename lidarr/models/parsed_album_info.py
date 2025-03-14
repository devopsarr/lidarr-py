# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.9.6.4552
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from lidarr.models.artist_title_info import ArtistTitleInfo
from lidarr.models.quality_model import QualityModel
from typing import Optional, Set
from typing_extensions import Self

class ParsedAlbumInfo(BaseModel):
    """
    ParsedAlbumInfo
    """ # noqa: E501
    release_title: Optional[StrictStr] = Field(default=None, alias="releaseTitle")
    album_title: Optional[StrictStr] = Field(default=None, alias="albumTitle")
    artist_name: Optional[StrictStr] = Field(default=None, alias="artistName")
    album_type: Optional[StrictStr] = Field(default=None, alias="albumType")
    artist_title_info: Optional[ArtistTitleInfo] = Field(default=None, alias="artistTitleInfo")
    quality: Optional[QualityModel] = None
    release_date: Optional[StrictStr] = Field(default=None, alias="releaseDate")
    discography: Optional[StrictBool] = None
    discography_start: Optional[StrictInt] = Field(default=None, alias="discographyStart")
    discography_end: Optional[StrictInt] = Field(default=None, alias="discographyEnd")
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    release_hash: Optional[StrictStr] = Field(default=None, alias="releaseHash")
    release_version: Optional[StrictStr] = Field(default=None, alias="releaseVersion")
    __properties: ClassVar[List[str]] = ["releaseTitle", "albumTitle", "artistName", "albumType", "artistTitleInfo", "quality", "releaseDate", "discography", "discographyStart", "discographyEnd", "releaseGroup", "releaseHash", "releaseVersion"]

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
        """Create an instance of ParsedAlbumInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of artist_title_info
        if self.artist_title_info:
            _dict['artistTitleInfo'] = self.artist_title_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # set to None if release_title (nullable) is None
        # and model_fields_set contains the field
        if self.release_title is None and "release_title" in self.model_fields_set:
            _dict['releaseTitle'] = None

        # set to None if album_title (nullable) is None
        # and model_fields_set contains the field
        if self.album_title is None and "album_title" in self.model_fields_set:
            _dict['albumTitle'] = None

        # set to None if artist_name (nullable) is None
        # and model_fields_set contains the field
        if self.artist_name is None and "artist_name" in self.model_fields_set:
            _dict['artistName'] = None

        # set to None if album_type (nullable) is None
        # and model_fields_set contains the field
        if self.album_type is None and "album_type" in self.model_fields_set:
            _dict['albumType'] = None

        # set to None if release_date (nullable) is None
        # and model_fields_set contains the field
        if self.release_date is None and "release_date" in self.model_fields_set:
            _dict['releaseDate'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if release_hash (nullable) is None
        # and model_fields_set contains the field
        if self.release_hash is None and "release_hash" in self.model_fields_set:
            _dict['releaseHash'] = None

        # set to None if release_version (nullable) is None
        # and model_fields_set contains the field
        if self.release_version is None and "release_version" in self.model_fields_set:
            _dict['releaseVersion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParsedAlbumInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "releaseTitle": obj.get("releaseTitle"),
            "albumTitle": obj.get("albumTitle"),
            "artistName": obj.get("artistName"),
            "albumType": obj.get("albumType"),
            "artistTitleInfo": ArtistTitleInfo.from_dict(obj["artistTitleInfo"]) if obj.get("artistTitleInfo") is not None else None,
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "releaseDate": obj.get("releaseDate"),
            "discography": obj.get("discography"),
            "discographyStart": obj.get("discographyStart"),
            "discographyEnd": obj.get("discographyEnd"),
            "releaseGroup": obj.get("releaseGroup"),
            "releaseHash": obj.get("releaseHash"),
            "releaseVersion": obj.get("releaseVersion")
        })
        return _obj


