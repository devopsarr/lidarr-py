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



from pydantic import BaseModel
from lidarr.models.add_album_options import AddAlbumOptions
from lidarr.models.album_release_resource import AlbumReleaseResource
from lidarr.models.album_statistics_resource import AlbumStatisticsResource
from lidarr.models.links import Links
from lidarr.models.media_cover import MediaCover
from lidarr.models.medium_resource import MediumResource
from lidarr.models.ratings import Ratings

class AlbumResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    title: Optional[str]
    disambiguation: Optional[str]
    overview: Optional[str]
    artist_id: Optional[int]
    foreign_album_id: Optional[str]
    monitored: Optional[bool]
    any_release_ok: Optional[bool]
    profile_id: Optional[int]
    duration: Optional[int]
    album_type: Optional[str]
    secondary_types: Optional[List]
    medium_count: Optional[int]
    ratings: Optional[Ratings]
    release_date: Optional[datetime]
    releases: Optional[List]
    genres: Optional[List]
    media: Optional[List]
    artist: Optional[ArtistResource]
    images: Optional[List]
    links: Optional[List]
    statistics: Optional[AlbumStatisticsResource]
    add_options: Optional[AddAlbumOptions]
    remote_cover: Optional[str]
    grabbed: Optional[bool]
    __properties = ["id", "title", "disambiguation", "overview", "artistId", "foreignAlbumId", "monitored", "anyReleaseOk", "profileId", "duration", "albumType", "secondaryTypes", "mediumCount", "ratings", "releaseDate", "releases", "genres", "media", "artist", "images", "links", "statistics", "addOptions", "remoteCover", "grabbed"]

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
    def from_json(cls, json_str: str) -> AlbumResource:
        """Create an instance of AlbumResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "medium_count",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in releases (list)
        _items = []
        if self.releases:
            for _item in self.releases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['releases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in media (list)
        _items = []
        if self.media:
            for _item in self.media:
                if _item:
                    _items.append(_item.to_dict())
            _dict['media'] = _items
        # override the default output from pydantic by calling `to_dict()` of artist
        if self.artist:
            _dict['artist'] = self.artist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of add_options
        if self.add_options:
            _dict['addOptions'] = self.add_options.to_dict()
        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if disambiguation (nullable) is None
        if self.disambiguation is None:
            _dict['disambiguation'] = None

        # set to None if overview (nullable) is None
        if self.overview is None:
            _dict['overview'] = None

        # set to None if foreign_album_id (nullable) is None
        if self.foreign_album_id is None:
            _dict['foreignAlbumId'] = None

        # set to None if album_type (nullable) is None
        if self.album_type is None:
            _dict['albumType'] = None

        # set to None if secondary_types (nullable) is None
        if self.secondary_types is None:
            _dict['secondaryTypes'] = None

        # set to None if release_date (nullable) is None
        if self.release_date is None:
            _dict['releaseDate'] = None

        # set to None if releases (nullable) is None
        if self.releases is None:
            _dict['releases'] = None

        # set to None if genres (nullable) is None
        if self.genres is None:
            _dict['genres'] = None

        # set to None if media (nullable) is None
        if self.media is None:
            _dict['media'] = None

        # set to None if images (nullable) is None
        if self.images is None:
            _dict['images'] = None

        # set to None if links (nullable) is None
        if self.links is None:
            _dict['links'] = None

        # set to None if remote_cover (nullable) is None
        if self.remote_cover is None:
            _dict['remoteCover'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlbumResource:
        """Create an instance of AlbumResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AlbumResource.parse_obj(obj)

        _obj = AlbumResource.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "disambiguation": obj.get("disambiguation"),
            "overview": obj.get("overview"),
            "artist_id": obj.get("artistId"),
            "foreign_album_id": obj.get("foreignAlbumId"),
            "monitored": obj.get("monitored"),
            "any_release_ok": obj.get("anyReleaseOk"),
            "profile_id": obj.get("profileId"),
            "duration": obj.get("duration"),
            "album_type": obj.get("albumType"),
            "secondary_types": obj.get("secondaryTypes"),
            "medium_count": obj.get("mediumCount"),
            "ratings": Ratings.from_dict(obj.get("ratings")) if obj.get("ratings") is not None else None,
            "release_date": obj.get("releaseDate"),
            "releases": [AlbumReleaseResource.from_dict(_item) for _item in obj.get("releases")] if obj.get("releases") is not None else None,
            "genres": obj.get("genres"),
            "media": [MediumResource.from_dict(_item) for _item in obj.get("media")] if obj.get("media") is not None else None,
            "artist": ArtistResource.from_dict(obj.get("artist")) if obj.get("artist") is not None else None,
            "images": [MediaCover.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "links": [Links.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "statistics": AlbumStatisticsResource.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None,
            "add_options": AddAlbumOptions.from_dict(obj.get("addOptions")) if obj.get("addOptions") is not None else None,
            "remote_cover": obj.get("remoteCover"),
            "grabbed": obj.get("grabbed")
        })
        return _obj

