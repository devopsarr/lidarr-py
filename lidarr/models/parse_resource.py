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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.album_resource import AlbumResource
from lidarr.models.artist_resource import ArtistResource
from lidarr.models.custom_format_resource import CustomFormatResource
from lidarr.models.parsed_album_info import ParsedAlbumInfo
from typing import Optional, Set
from typing_extensions import Self

class ParseResource(BaseModel):
    """
    ParseResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    parsed_album_info: Optional[ParsedAlbumInfo] = Field(default=None, alias="parsedAlbumInfo")
    artist: Optional[ArtistResource] = None
    albums: Optional[List[AlbumResource]] = None
    custom_formats: Optional[List[CustomFormatResource]] = Field(default=None, alias="customFormats")
    custom_format_score: Optional[StrictInt] = Field(default=None, alias="customFormatScore")
    __properties: ClassVar[List[str]] = ["id", "title", "parsedAlbumInfo", "artist", "albums", "customFormats", "customFormatScore"]

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
        """Create an instance of ParseResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parsed_album_info
        if self.parsed_album_info:
            _dict['parsedAlbumInfo'] = self.parsed_album_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of artist
        if self.artist:
            _dict['artist'] = self.artist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in albums (list)
        _items = []
        if self.albums:
            for _item in self.albums:
                if _item:
                    _items.append(_item.to_dict())
            _dict['albums'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if albums (nullable) is None
        # and model_fields_set contains the field
        if self.albums is None and "albums" in self.model_fields_set:
            _dict['albums'] = None

        # set to None if custom_formats (nullable) is None
        # and model_fields_set contains the field
        if self.custom_formats is None and "custom_formats" in self.model_fields_set:
            _dict['customFormats'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParseResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "parsedAlbumInfo": ParsedAlbumInfo.from_dict(obj["parsedAlbumInfo"]) if obj.get("parsedAlbumInfo") is not None else None,
            "artist": ArtistResource.from_dict(obj["artist"]) if obj.get("artist") is not None else None,
            "albums": [AlbumResource.from_dict(_item) for _item in obj["albums"]] if obj.get("albums") is not None else None,
            "customFormats": [CustomFormatResource.from_dict(_item) for _item in obj["customFormats"]] if obj.get("customFormats") is not None else None,
            "customFormatScore": obj.get("customFormatScore")
        })
        return _obj


