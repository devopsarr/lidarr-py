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


from typing import Optional
from pydantic import BaseModel
from lidarr.models.artist_resource import ArtistResource
from lidarr.models.ratings import Ratings
from lidarr.models.track_file_resource import TrackFileResource

class TrackResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    artist_id: Optional[int]
    foreign_track_id: Optional[str]
    foreign_recording_id: Optional[str]
    track_file_id: Optional[int]
    album_id: Optional[int]
    explicit: Optional[bool]
    absolute_track_number: Optional[int]
    track_number: Optional[str]
    title: Optional[str]
    duration: Optional[int]
    track_file: Optional[TrackFileResource]
    medium_number: Optional[int]
    has_file: Optional[bool]
    artist: Optional[ArtistResource]
    ratings: Optional[Ratings]
    grabbed: Optional[bool]
    __properties = ["id", "artistId", "foreignTrackId", "foreignRecordingId", "trackFileId", "albumId", "explicit", "absoluteTrackNumber", "trackNumber", "title", "duration", "trackFile", "mediumNumber", "hasFile", "artist", "ratings", "grabbed"]

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
    def from_json(cls, json_str: str) -> TrackResource:
        """Create an instance of TrackResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of track_file
        if self.track_file:
            _dict['trackFile'] = self.track_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of artist
        if self.artist:
            _dict['artist'] = self.artist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # set to None if foreign_track_id (nullable) is None
        if self.foreign_track_id is None:
            _dict['foreignTrackId'] = None

        # set to None if foreign_recording_id (nullable) is None
        if self.foreign_recording_id is None:
            _dict['foreignRecordingId'] = None

        # set to None if track_number (nullable) is None
        if self.track_number is None:
            _dict['trackNumber'] = None

        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrackResource:
        """Create an instance of TrackResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TrackResource.parse_obj(obj)

        _obj = TrackResource.parse_obj({
            "id": obj.get("id"),
            "artist_id": obj.get("artistId"),
            "foreign_track_id": obj.get("foreignTrackId"),
            "foreign_recording_id": obj.get("foreignRecordingId"),
            "track_file_id": obj.get("trackFileId"),
            "album_id": obj.get("albumId"),
            "explicit": obj.get("explicit"),
            "absolute_track_number": obj.get("absoluteTrackNumber"),
            "track_number": obj.get("trackNumber"),
            "title": obj.get("title"),
            "duration": obj.get("duration"),
            "track_file": TrackFileResource.from_dict(obj.get("trackFile")) if obj.get("trackFile") is not None else None,
            "medium_number": obj.get("mediumNumber"),
            "has_file": obj.get("hasFile"),
            "artist": ArtistResource.from_dict(obj.get("artist")) if obj.get("artist") is not None else None,
            "ratings": Ratings.from_dict(obj.get("ratings")) if obj.get("ratings") is not None else None,
            "grabbed": obj.get("grabbed")
        })
        return _obj

