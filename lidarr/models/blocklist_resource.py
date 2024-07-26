# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.4.3.4248
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.artist_resource import ArtistResource
from lidarr.models.custom_format_resource import CustomFormatResource
from lidarr.models.download_protocol import DownloadProtocol
from lidarr.models.quality_model import QualityModel
from typing import Optional, Set
from typing_extensions import Self

class BlocklistResource(BaseModel):
    """
    BlocklistResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    artist_id: Optional[StrictInt] = Field(default=None, alias="artistId")
    album_ids: Optional[List[StrictInt]] = Field(default=None, alias="albumIds")
    source_title: Optional[StrictStr] = Field(default=None, alias="sourceTitle")
    quality: Optional[QualityModel] = None
    custom_formats: Optional[List[CustomFormatResource]] = Field(default=None, alias="customFormats")
    var_date: Optional[datetime] = Field(default=None, alias="date")
    protocol: Optional[DownloadProtocol] = None
    indexer: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    artist: Optional[ArtistResource] = None
    __properties: ClassVar[List[str]] = ["id", "artistId", "albumIds", "sourceTitle", "quality", "customFormats", "date", "protocol", "indexer", "message", "artist"]

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
        """Create an instance of BlocklistResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of artist
        if self.artist:
            _dict['artist'] = self.artist.to_dict()
        # set to None if album_ids (nullable) is None
        # and model_fields_set contains the field
        if self.album_ids is None and "album_ids" in self.model_fields_set:
            _dict['albumIds'] = None

        # set to None if source_title (nullable) is None
        # and model_fields_set contains the field
        if self.source_title is None and "source_title" in self.model_fields_set:
            _dict['sourceTitle'] = None

        # set to None if custom_formats (nullable) is None
        # and model_fields_set contains the field
        if self.custom_formats is None and "custom_formats" in self.model_fields_set:
            _dict['customFormats'] = None

        # set to None if indexer (nullable) is None
        # and model_fields_set contains the field
        if self.indexer is None and "indexer" in self.model_fields_set:
            _dict['indexer'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BlocklistResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "artistId": obj.get("artistId"),
            "albumIds": obj.get("albumIds"),
            "sourceTitle": obj.get("sourceTitle"),
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "customFormats": [CustomFormatResource.from_dict(_item) for _item in obj["customFormats"]] if obj.get("customFormats") is not None else None,
            "date": obj.get("date"),
            "protocol": obj.get("protocol"),
            "indexer": obj.get("indexer"),
            "message": obj.get("message"),
            "artist": ArtistResource.from_dict(obj["artist"]) if obj.get("artist") is not None else None
        })
        return _obj


