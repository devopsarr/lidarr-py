# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.6.4.4402
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.custom_format_resource import CustomFormatResource
from lidarr.models.media_info_resource import MediaInfoResource
from lidarr.models.parsed_track_info import ParsedTrackInfo
from lidarr.models.quality_model import QualityModel
from typing import Optional, Set
from typing_extensions import Self

class TrackFileResource(BaseModel):
    """
    TrackFileResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    artist_id: Optional[StrictInt] = Field(default=None, alias="artistId")
    album_id: Optional[StrictInt] = Field(default=None, alias="albumId")
    path: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    date_added: Optional[datetime] = Field(default=None, alias="dateAdded")
    scene_name: Optional[StrictStr] = Field(default=None, alias="sceneName")
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    quality: Optional[QualityModel] = None
    quality_weight: Optional[StrictInt] = Field(default=None, alias="qualityWeight")
    custom_formats: Optional[List[CustomFormatResource]] = Field(default=None, alias="customFormats")
    custom_format_score: Optional[StrictInt] = Field(default=None, alias="customFormatScore")
    indexer_flags: Optional[StrictInt] = Field(default=None, alias="indexerFlags")
    media_info: Optional[MediaInfoResource] = Field(default=None, alias="mediaInfo")
    quality_cutoff_not_met: Optional[StrictBool] = Field(default=None, alias="qualityCutoffNotMet")
    audio_tags: Optional[ParsedTrackInfo] = Field(default=None, alias="audioTags")
    __properties: ClassVar[List[str]] = ["id", "artistId", "albumId", "path", "size", "dateAdded", "sceneName", "releaseGroup", "quality", "qualityWeight", "customFormats", "customFormatScore", "indexerFlags", "mediaInfo", "qualityCutoffNotMet", "audioTags"]

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
        """Create an instance of TrackFileResource from a JSON string"""
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
            for _item_custom_formats in self.custom_formats:
                if _item_custom_formats:
                    _items.append(_item_custom_formats.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of audio_tags
        if self.audio_tags:
            _dict['audioTags'] = self.audio_tags.to_dict()
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if scene_name (nullable) is None
        # and model_fields_set contains the field
        if self.scene_name is None and "scene_name" in self.model_fields_set:
            _dict['sceneName'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if custom_formats (nullable) is None
        # and model_fields_set contains the field
        if self.custom_formats is None and "custom_formats" in self.model_fields_set:
            _dict['customFormats'] = None

        # set to None if indexer_flags (nullable) is None
        # and model_fields_set contains the field
        if self.indexer_flags is None and "indexer_flags" in self.model_fields_set:
            _dict['indexerFlags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackFileResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "artistId": obj.get("artistId"),
            "albumId": obj.get("albumId"),
            "path": obj.get("path"),
            "size": obj.get("size"),
            "dateAdded": obj.get("dateAdded"),
            "sceneName": obj.get("sceneName"),
            "releaseGroup": obj.get("releaseGroup"),
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "qualityWeight": obj.get("qualityWeight"),
            "customFormats": [CustomFormatResource.from_dict(_item) for _item in obj["customFormats"]] if obj.get("customFormats") is not None else None,
            "customFormatScore": obj.get("customFormatScore"),
            "indexerFlags": obj.get("indexerFlags"),
            "mediaInfo": MediaInfoResource.from_dict(obj["mediaInfo"]) if obj.get("mediaInfo") is not None else None,
            "qualityCutoffNotMet": obj.get("qualityCutoffNotMet"),
            "audioTags": ParsedTrackInfo.from_dict(obj["audioTags"]) if obj.get("audioTags") is not None else None
        })
        return _obj


