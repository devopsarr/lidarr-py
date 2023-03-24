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
from typing import List, Optional
from pydantic import BaseModel
from lidarr.models.custom_format_resource import CustomFormatResource
from lidarr.models.download_protocol import DownloadProtocol
from lidarr.models.quality_model import QualityModel

class ReleaseResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    guid: Optional[str]
    quality: Optional[QualityModel]
    quality_weight: Optional[int]
    age: Optional[int]
    age_hours: Optional[float]
    age_minutes: Optional[float]
    size: Optional[int]
    indexer_id: Optional[int]
    indexer: Optional[str]
    release_group: Optional[str]
    sub_group: Optional[str]
    release_hash: Optional[str]
    title: Optional[str]
    discography: Optional[bool]
    scene_source: Optional[bool]
    air_date: Optional[str]
    artist_name: Optional[str]
    album_title: Optional[str]
    approved: Optional[bool]
    temporarily_rejected: Optional[bool]
    rejected: Optional[bool]
    rejections: Optional[List]
    publish_date: Optional[datetime]
    comment_url: Optional[str]
    download_url: Optional[str]
    info_url: Optional[str]
    download_allowed: Optional[bool]
    release_weight: Optional[int]
    custom_formats: Optional[List]
    custom_format_score: Optional[int]
    magnet_url: Optional[str]
    info_hash: Optional[str]
    seeders: Optional[int]
    leechers: Optional[int]
    protocol: Optional[DownloadProtocol]
    artist_id: Optional[int]
    album_id: Optional[int]
    __properties = ["id", "guid", "quality", "qualityWeight", "age", "ageHours", "ageMinutes", "size", "indexerId", "indexer", "releaseGroup", "subGroup", "releaseHash", "title", "discography", "sceneSource", "airDate", "artistName", "albumTitle", "approved", "temporarilyRejected", "rejected", "rejections", "publishDate", "commentUrl", "downloadUrl", "infoUrl", "downloadAllowed", "releaseWeight", "customFormats", "customFormatScore", "magnetUrl", "infoHash", "seeders", "leechers", "protocol", "artistId", "albumId"]

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
    def from_json(cls, json_str: str) -> ReleaseResource:
        """Create an instance of ReleaseResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # set to None if guid (nullable) is None
        if self.guid is None:
            _dict['guid'] = None

        # set to None if indexer (nullable) is None
        if self.indexer is None:
            _dict['indexer'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if sub_group (nullable) is None
        if self.sub_group is None:
            _dict['subGroup'] = None

        # set to None if release_hash (nullable) is None
        if self.release_hash is None:
            _dict['releaseHash'] = None

        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if air_date (nullable) is None
        if self.air_date is None:
            _dict['airDate'] = None

        # set to None if artist_name (nullable) is None
        if self.artist_name is None:
            _dict['artistName'] = None

        # set to None if album_title (nullable) is None
        if self.album_title is None:
            _dict['albumTitle'] = None

        # set to None if rejections (nullable) is None
        if self.rejections is None:
            _dict['rejections'] = None

        # set to None if comment_url (nullable) is None
        if self.comment_url is None:
            _dict['commentUrl'] = None

        # set to None if download_url (nullable) is None
        if self.download_url is None:
            _dict['downloadUrl'] = None

        # set to None if info_url (nullable) is None
        if self.info_url is None:
            _dict['infoUrl'] = None

        # set to None if custom_formats (nullable) is None
        if self.custom_formats is None:
            _dict['customFormats'] = None

        # set to None if magnet_url (nullable) is None
        if self.magnet_url is None:
            _dict['magnetUrl'] = None

        # set to None if info_hash (nullable) is None
        if self.info_hash is None:
            _dict['infoHash'] = None

        # set to None if seeders (nullable) is None
        if self.seeders is None:
            _dict['seeders'] = None

        # set to None if leechers (nullable) is None
        if self.leechers is None:
            _dict['leechers'] = None

        # set to None if artist_id (nullable) is None
        if self.artist_id is None:
            _dict['artistId'] = None

        # set to None if album_id (nullable) is None
        if self.album_id is None:
            _dict['albumId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReleaseResource:
        """Create an instance of ReleaseResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ReleaseResource.parse_obj(obj)

        _obj = ReleaseResource.parse_obj({
            "id": obj.get("id"),
            "guid": obj.get("guid"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "quality_weight": obj.get("qualityWeight"),
            "age": obj.get("age"),
            "age_hours": obj.get("ageHours"),
            "age_minutes": obj.get("ageMinutes"),
            "size": obj.get("size"),
            "indexer_id": obj.get("indexerId"),
            "indexer": obj.get("indexer"),
            "release_group": obj.get("releaseGroup"),
            "sub_group": obj.get("subGroup"),
            "release_hash": obj.get("releaseHash"),
            "title": obj.get("title"),
            "discography": obj.get("discography"),
            "scene_source": obj.get("sceneSource"),
            "air_date": obj.get("airDate"),
            "artist_name": obj.get("artistName"),
            "album_title": obj.get("albumTitle"),
            "approved": obj.get("approved"),
            "temporarily_rejected": obj.get("temporarilyRejected"),
            "rejected": obj.get("rejected"),
            "rejections": obj.get("rejections"),
            "publish_date": obj.get("publishDate"),
            "comment_url": obj.get("commentUrl"),
            "download_url": obj.get("downloadUrl"),
            "info_url": obj.get("infoUrl"),
            "download_allowed": obj.get("downloadAllowed"),
            "release_weight": obj.get("releaseWeight"),
            "custom_formats": [CustomFormatResource.from_dict(_item) for _item in obj.get("customFormats")] if obj.get("customFormats") is not None else None,
            "custom_format_score": obj.get("customFormatScore"),
            "magnet_url": obj.get("magnetUrl"),
            "info_hash": obj.get("infoHash"),
            "seeders": obj.get("seeders"),
            "leechers": obj.get("leechers"),
            "protocol": obj.get("protocol"),
            "artist_id": obj.get("artistId"),
            "album_id": obj.get("albumId")
        })
        return _obj

