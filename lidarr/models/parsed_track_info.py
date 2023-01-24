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


from typing import List, Optional
from pydantic import BaseModel
from lidarr.models.artist_title_info import ArtistTitleInfo
from lidarr.models.iso_country import IsoCountry
from lidarr.models.media_info_model import MediaInfoModel
from lidarr.models.quality_model import QualityModel
from lidarr.models.time_span import TimeSpan

class ParsedTrackInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    title: Optional[str]
    clean_title: Optional[str]
    artist_title: Optional[str]
    album_title: Optional[str]
    artist_title_info: Optional[ArtistTitleInfo]
    artist_mbid: Optional[str]
    album_mbid: Optional[str]
    release_mbid: Optional[str]
    recording_mbid: Optional[str]
    track_mbid: Optional[str]
    disc_number: Optional[int]
    disc_count: Optional[int]
    country: Optional[IsoCountry]
    year: Optional[int]
    label: Optional[str]
    catalog_number: Optional[str]
    disambiguation: Optional[str]
    duration: Optional[TimeSpan]
    quality: Optional[QualityModel]
    media_info: Optional[MediaInfoModel]
    track_numbers: Optional[List]
    release_group: Optional[str]
    release_hash: Optional[str]
    __properties = ["title", "cleanTitle", "artistTitle", "albumTitle", "artistTitleInfo", "artistMBId", "albumMBId", "releaseMBId", "recordingMBId", "trackMBId", "discNumber", "discCount", "country", "year", "label", "catalogNumber", "disambiguation", "duration", "quality", "mediaInfo", "trackNumbers", "releaseGroup", "releaseHash"]

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
    def from_json(cls, json_str: str) -> ParsedTrackInfo:
        """Create an instance of ParsedTrackInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of artist_title_info
        if self.artist_title_info:
            _dict['artistTitleInfo'] = self.artist_title_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['country'] = self.country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if clean_title (nullable) is None
        if self.clean_title is None:
            _dict['cleanTitle'] = None

        # set to None if artist_title (nullable) is None
        if self.artist_title is None:
            _dict['artistTitle'] = None

        # set to None if album_title (nullable) is None
        if self.album_title is None:
            _dict['albumTitle'] = None

        # set to None if artist_mbid (nullable) is None
        if self.artist_mbid is None:
            _dict['artistMBId'] = None

        # set to None if album_mbid (nullable) is None
        if self.album_mbid is None:
            _dict['albumMBId'] = None

        # set to None if release_mbid (nullable) is None
        if self.release_mbid is None:
            _dict['releaseMBId'] = None

        # set to None if recording_mbid (nullable) is None
        if self.recording_mbid is None:
            _dict['recordingMBId'] = None

        # set to None if track_mbid (nullable) is None
        if self.track_mbid is None:
            _dict['trackMBId'] = None

        # set to None if label (nullable) is None
        if self.label is None:
            _dict['label'] = None

        # set to None if catalog_number (nullable) is None
        if self.catalog_number is None:
            _dict['catalogNumber'] = None

        # set to None if disambiguation (nullable) is None
        if self.disambiguation is None:
            _dict['disambiguation'] = None

        # set to None if track_numbers (nullable) is None
        if self.track_numbers is None:
            _dict['trackNumbers'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if release_hash (nullable) is None
        if self.release_hash is None:
            _dict['releaseHash'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParsedTrackInfo:
        """Create an instance of ParsedTrackInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ParsedTrackInfo.parse_obj(obj)

        _obj = ParsedTrackInfo.parse_obj({
            "title": obj.get("title"),
            "clean_title": obj.get("cleanTitle"),
            "artist_title": obj.get("artistTitle"),
            "album_title": obj.get("albumTitle"),
            "artist_title_info": ArtistTitleInfo.from_dict(obj.get("artistTitleInfo")) if obj.get("artistTitleInfo") is not None else None,
            "artist_mbid": obj.get("artistMBId"),
            "album_mbid": obj.get("albumMBId"),
            "release_mbid": obj.get("releaseMBId"),
            "recording_mbid": obj.get("recordingMBId"),
            "track_mbid": obj.get("trackMBId"),
            "disc_number": obj.get("discNumber"),
            "disc_count": obj.get("discCount"),
            "country": IsoCountry.from_dict(obj.get("country")) if obj.get("country") is not None else None,
            "year": obj.get("year"),
            "label": obj.get("label"),
            "catalog_number": obj.get("catalogNumber"),
            "disambiguation": obj.get("disambiguation"),
            "duration": TimeSpan.from_dict(obj.get("duration")) if obj.get("duration") is not None else None,
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "media_info": MediaInfoModel.from_dict(obj.get("mediaInfo")) if obj.get("mediaInfo") is not None else None,
            "track_numbers": obj.get("trackNumbers"),
            "release_group": obj.get("releaseGroup"),
            "release_hash": obj.get("releaseHash")
        })
        return _obj

