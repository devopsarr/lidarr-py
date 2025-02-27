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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.add_album_options import AddAlbumOptions
from lidarr.models.album_release_resource import AlbumReleaseResource
from lidarr.models.album_statistics_resource import AlbumStatisticsResource
from lidarr.models.links import Links
from lidarr.models.media_cover import MediaCover
from lidarr.models.medium_resource import MediumResource
from lidarr.models.ratings import Ratings
from typing import Optional, Set
from typing_extensions import Self

class AlbumResource(BaseModel):
    """
    AlbumResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    disambiguation: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    artist_id: Optional[StrictInt] = Field(default=None, alias="artistId")
    foreign_album_id: Optional[StrictStr] = Field(default=None, alias="foreignAlbumId")
    monitored: Optional[StrictBool] = None
    any_release_ok: Optional[StrictBool] = Field(default=None, alias="anyReleaseOk")
    profile_id: Optional[StrictInt] = Field(default=None, alias="profileId")
    duration: Optional[StrictInt] = None
    album_type: Optional[StrictStr] = Field(default=None, alias="albumType")
    secondary_types: Optional[List[StrictStr]] = Field(default=None, alias="secondaryTypes")
    medium_count: Optional[StrictInt] = Field(default=None, alias="mediumCount")
    ratings: Optional[Ratings] = None
    release_date: Optional[datetime] = Field(default=None, alias="releaseDate")
    releases: Optional[List[AlbumReleaseResource]] = None
    genres: Optional[List[StrictStr]] = None
    media: Optional[List[MediumResource]] = None
    artist: Optional[ArtistResource] = None
    images: Optional[List[MediaCover]] = None
    links: Optional[List[Links]] = None
    last_search_time: Optional[datetime] = Field(default=None, alias="lastSearchTime")
    statistics: Optional[AlbumStatisticsResource] = None
    add_options: Optional[AddAlbumOptions] = Field(default=None, alias="addOptions")
    remote_cover: Optional[StrictStr] = Field(default=None, alias="remoteCover")
    __properties: ClassVar[List[str]] = ["id", "title", "disambiguation", "overview", "artistId", "foreignAlbumId", "monitored", "anyReleaseOk", "profileId", "duration", "albumType", "secondaryTypes", "mediumCount", "ratings", "releaseDate", "releases", "genres", "media", "artist", "images", "links", "lastSearchTime", "statistics", "addOptions", "remoteCover"]

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
        """Create an instance of AlbumResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "medium_count",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in releases (list)
        _items = []
        if self.releases:
            for _item_releases in self.releases:
                if _item_releases:
                    _items.append(_item_releases.to_dict())
            _dict['releases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in media (list)
        _items = []
        if self.media:
            for _item_media in self.media:
                if _item_media:
                    _items.append(_item_media.to_dict())
            _dict['media'] = _items
        # override the default output from pydantic by calling `to_dict()` of artist
        if self.artist:
            _dict['artist'] = self.artist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of add_options
        if self.add_options:
            _dict['addOptions'] = self.add_options.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if disambiguation (nullable) is None
        # and model_fields_set contains the field
        if self.disambiguation is None and "disambiguation" in self.model_fields_set:
            _dict['disambiguation'] = None

        # set to None if overview (nullable) is None
        # and model_fields_set contains the field
        if self.overview is None and "overview" in self.model_fields_set:
            _dict['overview'] = None

        # set to None if foreign_album_id (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_album_id is None and "foreign_album_id" in self.model_fields_set:
            _dict['foreignAlbumId'] = None

        # set to None if album_type (nullable) is None
        # and model_fields_set contains the field
        if self.album_type is None and "album_type" in self.model_fields_set:
            _dict['albumType'] = None

        # set to None if secondary_types (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_types is None and "secondary_types" in self.model_fields_set:
            _dict['secondaryTypes'] = None

        # set to None if release_date (nullable) is None
        # and model_fields_set contains the field
        if self.release_date is None and "release_date" in self.model_fields_set:
            _dict['releaseDate'] = None

        # set to None if releases (nullable) is None
        # and model_fields_set contains the field
        if self.releases is None and "releases" in self.model_fields_set:
            _dict['releases'] = None

        # set to None if genres (nullable) is None
        # and model_fields_set contains the field
        if self.genres is None and "genres" in self.model_fields_set:
            _dict['genres'] = None

        # set to None if media (nullable) is None
        # and model_fields_set contains the field
        if self.media is None and "media" in self.model_fields_set:
            _dict['media'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if last_search_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_search_time is None and "last_search_time" in self.model_fields_set:
            _dict['lastSearchTime'] = None

        # set to None if remote_cover (nullable) is None
        # and model_fields_set contains the field
        if self.remote_cover is None and "remote_cover" in self.model_fields_set:
            _dict['remoteCover'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlbumResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "disambiguation": obj.get("disambiguation"),
            "overview": obj.get("overview"),
            "artistId": obj.get("artistId"),
            "foreignAlbumId": obj.get("foreignAlbumId"),
            "monitored": obj.get("monitored"),
            "anyReleaseOk": obj.get("anyReleaseOk"),
            "profileId": obj.get("profileId"),
            "duration": obj.get("duration"),
            "albumType": obj.get("albumType"),
            "secondaryTypes": obj.get("secondaryTypes"),
            "mediumCount": obj.get("mediumCount"),
            "ratings": Ratings.from_dict(obj["ratings"]) if obj.get("ratings") is not None else None,
            "releaseDate": obj.get("releaseDate"),
            "releases": [AlbumReleaseResource.from_dict(_item) for _item in obj["releases"]] if obj.get("releases") is not None else None,
            "genres": obj.get("genres"),
            "media": [MediumResource.from_dict(_item) for _item in obj["media"]] if obj.get("media") is not None else None,
            "artist": ArtistResource.from_dict(obj["artist"]) if obj.get("artist") is not None else None,
            "images": [MediaCover.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "links": [Links.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "lastSearchTime": obj.get("lastSearchTime"),
            "statistics": AlbumStatisticsResource.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
            "addOptions": AddAlbumOptions.from_dict(obj["addOptions"]) if obj.get("addOptions") is not None else None,
            "remoteCover": obj.get("remoteCover")
        })
        return _obj

from lidarr.models.artist_resource import ArtistResource
# TODO: Rewrite to not use raise_errors
AlbumResource.model_rebuild(raise_errors=False)

