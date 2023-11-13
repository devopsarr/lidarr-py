# coding: utf-8

"""
    Lidarr

    Lidarr API docs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, Optional
from pydantic import BaseModel
from lidarr.models.media_info_model import MediaInfoModel
from lidarr.models.quality_model import QualityModel

class TrackFile(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    path: Optional[str]
    size: Optional[int]
    modified: Optional[datetime]
    date_added: Optional[datetime]
    original_file_path: Optional[str]
    scene_name: Optional[str]
    release_group: Optional[str]
    quality: Optional[QualityModel]
    media_info: Optional[MediaInfoModel]
    album_id: Optional[int]
    tracks: Optional[TrackListLazyLoaded]
    artist: Optional[ArtistLazyLoaded]
    album: Optional[AlbumLazyLoaded]
    __properties = ["id", "path", "size", "modified", "dateAdded", "originalFilePath", "sceneName", "releaseGroup", "quality", "mediaInfo", "albumId", "tracks", "artist", "album"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TrackFile:
        """Create an instance of TrackFile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tracks
        if self.tracks:
            _dict['tracks'] = self.tracks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of artist
        if self.artist:
            _dict['artist'] = self.artist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of album
        if self.album:
            _dict['album'] = self.album.to_dict()
        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if original_file_path (nullable) is None
        if self.original_file_path is None:
            _dict['originalFilePath'] = None

        # set to None if scene_name (nullable) is None
        if self.scene_name is None:
            _dict['sceneName'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrackFile:
        """Create an instance of TrackFile from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TrackFile.parse_obj(obj)

        _obj = TrackFile.parse_obj({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "size": obj.get("size"),
            "modified": obj.get("modified"),
            "date_added": obj.get("dateAdded"),
            "original_file_path": obj.get("originalFilePath"),
            "scene_name": obj.get("sceneName"),
            "release_group": obj.get("releaseGroup"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "media_info": MediaInfoModel.from_dict(obj.get("mediaInfo")) if obj.get("mediaInfo") is not None else None,
            "album_id": obj.get("albumId"),
            "tracks": TrackListLazyLoaded.from_dict(obj.get("tracks")) if obj.get("tracks") is not None else None,
            "artist": ArtistLazyLoaded.from_dict(obj.get("artist")) if obj.get("artist") is not None else None,
            "album": AlbumLazyLoaded.from_dict(obj.get("album")) if obj.get("album") is not None else None
        })
        return _obj

