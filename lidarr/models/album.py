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
from lidarr.models.add_album_options import AddAlbumOptions
from lidarr.models.artist_metadata_lazy_loaded import ArtistMetadataLazyLoaded
from lidarr.models.links import Links
from lidarr.models.media_cover import MediaCover
from lidarr.models.ratings import Ratings
from lidarr.models.secondary_album_type import SecondaryAlbumType

class Album(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    artist_metadata_id: Optional[int]
    foreign_album_id: Optional[str]
    old_foreign_album_ids: Optional[List]
    title: Optional[str]
    overview: Optional[str]
    disambiguation: Optional[str]
    release_date: Optional[datetime]
    images: Optional[List]
    links: Optional[List]
    genres: Optional[List]
    album_type: Optional[str]
    secondary_types: Optional[List]
    ratings: Optional[Ratings]
    clean_title: Optional[str]
    profile_id: Optional[int]
    monitored: Optional[bool]
    any_release_ok: Optional[bool]
    last_info_sync: Optional[datetime]
    added: Optional[datetime]
    add_options: Optional[AddAlbumOptions]
    artist_metadata: Optional[ArtistMetadataLazyLoaded]
    album_releases: Optional[AlbumReleaseListLazyLoaded]
    artist: Optional[ArtistLazyLoaded]
    __properties = ["id", "artistMetadataId", "foreignAlbumId", "oldForeignAlbumIds", "title", "overview", "disambiguation", "releaseDate", "images", "links", "genres", "albumType", "secondaryTypes", "ratings", "cleanTitle", "profileId", "monitored", "anyReleaseOk", "lastInfoSync", "added", "addOptions", "artistMetadata", "albumReleases", "artist"]

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
    def from_json(cls, json_str: str) -> Album:
        """Create an instance of Album from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
        # override the default output from pydantic by calling `to_dict()` of each item in secondary_types (list)
        _items = []
        if self.secondary_types:
            for _item in self.secondary_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['secondaryTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of add_options
        if self.add_options:
            _dict['addOptions'] = self.add_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of artist_metadata
        if self.artist_metadata:
            _dict['artistMetadata'] = self.artist_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of album_releases
        if self.album_releases:
            _dict['albumReleases'] = self.album_releases.to_dict()
        # override the default output from pydantic by calling `to_dict()` of artist
        if self.artist:
            _dict['artist'] = self.artist.to_dict()
        # set to None if foreign_album_id (nullable) is None
        if self.foreign_album_id is None:
            _dict['foreignAlbumId'] = None

        # set to None if old_foreign_album_ids (nullable) is None
        if self.old_foreign_album_ids is None:
            _dict['oldForeignAlbumIds'] = None

        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if overview (nullable) is None
        if self.overview is None:
            _dict['overview'] = None

        # set to None if disambiguation (nullable) is None
        if self.disambiguation is None:
            _dict['disambiguation'] = None

        # set to None if release_date (nullable) is None
        if self.release_date is None:
            _dict['releaseDate'] = None

        # set to None if images (nullable) is None
        if self.images is None:
            _dict['images'] = None

        # set to None if links (nullable) is None
        if self.links is None:
            _dict['links'] = None

        # set to None if genres (nullable) is None
        if self.genres is None:
            _dict['genres'] = None

        # set to None if album_type (nullable) is None
        if self.album_type is None:
            _dict['albumType'] = None

        # set to None if secondary_types (nullable) is None
        if self.secondary_types is None:
            _dict['secondaryTypes'] = None

        # set to None if clean_title (nullable) is None
        if self.clean_title is None:
            _dict['cleanTitle'] = None

        # set to None if last_info_sync (nullable) is None
        if self.last_info_sync is None:
            _dict['lastInfoSync'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Album:
        """Create an instance of Album from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Album.parse_obj(obj)

        _obj = Album.parse_obj({
            "id": obj.get("id"),
            "artist_metadata_id": obj.get("artistMetadataId"),
            "foreign_album_id": obj.get("foreignAlbumId"),
            "old_foreign_album_ids": obj.get("oldForeignAlbumIds"),
            "title": obj.get("title"),
            "overview": obj.get("overview"),
            "disambiguation": obj.get("disambiguation"),
            "release_date": obj.get("releaseDate"),
            "images": [MediaCover.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "links": [Links.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "genres": obj.get("genres"),
            "album_type": obj.get("albumType"),
            "secondary_types": [SecondaryAlbumType.from_dict(_item) for _item in obj.get("secondaryTypes")] if obj.get("secondaryTypes") is not None else None,
            "ratings": Ratings.from_dict(obj.get("ratings")) if obj.get("ratings") is not None else None,
            "clean_title": obj.get("cleanTitle"),
            "profile_id": obj.get("profileId"),
            "monitored": obj.get("monitored"),
            "any_release_ok": obj.get("anyReleaseOk"),
            "last_info_sync": obj.get("lastInfoSync"),
            "added": obj.get("added"),
            "add_options": AddAlbumOptions.from_dict(obj.get("addOptions")) if obj.get("addOptions") is not None else None,
            "artist_metadata": ArtistMetadataLazyLoaded.from_dict(obj.get("artistMetadata")) if obj.get("artistMetadata") is not None else None,
            "album_releases": AlbumReleaseListLazyLoaded.from_dict(obj.get("albumReleases")) if obj.get("albumReleases") is not None else None,
            "artist": ArtistLazyLoaded.from_dict(obj.get("artist")) if obj.get("artist") is not None else None
        })
        return _obj

