# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.8.2.4493
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
from lidarr.models.add_artist_options import AddArtistOptions
from lidarr.models.artist_statistics_resource import ArtistStatisticsResource
from lidarr.models.artist_status_type import ArtistStatusType
from lidarr.models.links import Links
from lidarr.models.media_cover import MediaCover
from lidarr.models.member import Member
from lidarr.models.new_item_monitor_types import NewItemMonitorTypes
from lidarr.models.ratings import Ratings
from typing import Optional, Set
from typing_extensions import Self

class ArtistResource(BaseModel):
    """
    ArtistResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    status: Optional[ArtistStatusType] = None
    ended: Optional[StrictBool] = None
    artist_name: Optional[StrictStr] = Field(default=None, alias="artistName")
    foreign_artist_id: Optional[StrictStr] = Field(default=None, alias="foreignArtistId")
    mb_id: Optional[StrictStr] = Field(default=None, alias="mbId")
    tadb_id: Optional[StrictInt] = Field(default=None, alias="tadbId")
    discogs_id: Optional[StrictInt] = Field(default=None, alias="discogsId")
    all_music_id: Optional[StrictStr] = Field(default=None, alias="allMusicId")
    overview: Optional[StrictStr] = None
    artist_type: Optional[StrictStr] = Field(default=None, alias="artistType")
    disambiguation: Optional[StrictStr] = None
    links: Optional[List[Links]] = None
    next_album: Optional[AlbumResource] = Field(default=None, alias="nextAlbum")
    last_album: Optional[AlbumResource] = Field(default=None, alias="lastAlbum")
    images: Optional[List[MediaCover]] = None
    members: Optional[List[Member]] = None
    remote_poster: Optional[StrictStr] = Field(default=None, alias="remotePoster")
    path: Optional[StrictStr] = None
    quality_profile_id: Optional[StrictInt] = Field(default=None, alias="qualityProfileId")
    metadata_profile_id: Optional[StrictInt] = Field(default=None, alias="metadataProfileId")
    monitored: Optional[StrictBool] = None
    monitor_new_items: Optional[NewItemMonitorTypes] = Field(default=None, alias="monitorNewItems")
    root_folder_path: Optional[StrictStr] = Field(default=None, alias="rootFolderPath")
    folder: Optional[StrictStr] = None
    genres: Optional[List[StrictStr]] = None
    clean_name: Optional[StrictStr] = Field(default=None, alias="cleanName")
    sort_name: Optional[StrictStr] = Field(default=None, alias="sortName")
    tags: Optional[List[StrictInt]] = None
    added: Optional[datetime] = None
    add_options: Optional[AddArtistOptions] = Field(default=None, alias="addOptions")
    ratings: Optional[Ratings] = None
    statistics: Optional[ArtistStatisticsResource] = None
    __properties: ClassVar[List[str]] = ["id", "status", "ended", "artistName", "foreignArtistId", "mbId", "tadbId", "discogsId", "allMusicId", "overview", "artistType", "disambiguation", "links", "nextAlbum", "lastAlbum", "images", "members", "remotePoster", "path", "qualityProfileId", "metadataProfileId", "monitored", "monitorNewItems", "rootFolderPath", "folder", "genres", "cleanName", "sortName", "tags", "added", "addOptions", "ratings", "statistics"]

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
        """Create an instance of ArtistResource from a JSON string"""
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
            "ended",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of next_album
        if self.next_album:
            _dict['nextAlbum'] = self.next_album.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_album
        if self.last_album:
            _dict['lastAlbum'] = self.last_album.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item_members in self.members:
                if _item_members:
                    _items.append(_item_members.to_dict())
            _dict['members'] = _items
        # override the default output from pydantic by calling `to_dict()` of add_options
        if self.add_options:
            _dict['addOptions'] = self.add_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # set to None if artist_name (nullable) is None
        # and model_fields_set contains the field
        if self.artist_name is None and "artist_name" in self.model_fields_set:
            _dict['artistName'] = None

        # set to None if foreign_artist_id (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_artist_id is None and "foreign_artist_id" in self.model_fields_set:
            _dict['foreignArtistId'] = None

        # set to None if mb_id (nullable) is None
        # and model_fields_set contains the field
        if self.mb_id is None and "mb_id" in self.model_fields_set:
            _dict['mbId'] = None

        # set to None if all_music_id (nullable) is None
        # and model_fields_set contains the field
        if self.all_music_id is None and "all_music_id" in self.model_fields_set:
            _dict['allMusicId'] = None

        # set to None if overview (nullable) is None
        # and model_fields_set contains the field
        if self.overview is None and "overview" in self.model_fields_set:
            _dict['overview'] = None

        # set to None if artist_type (nullable) is None
        # and model_fields_set contains the field
        if self.artist_type is None and "artist_type" in self.model_fields_set:
            _dict['artistType'] = None

        # set to None if disambiguation (nullable) is None
        # and model_fields_set contains the field
        if self.disambiguation is None and "disambiguation" in self.model_fields_set:
            _dict['disambiguation'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if members (nullable) is None
        # and model_fields_set contains the field
        if self.members is None and "members" in self.model_fields_set:
            _dict['members'] = None

        # set to None if remote_poster (nullable) is None
        # and model_fields_set contains the field
        if self.remote_poster is None and "remote_poster" in self.model_fields_set:
            _dict['remotePoster'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if root_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.root_folder_path is None and "root_folder_path" in self.model_fields_set:
            _dict['rootFolderPath'] = None

        # set to None if folder (nullable) is None
        # and model_fields_set contains the field
        if self.folder is None and "folder" in self.model_fields_set:
            _dict['folder'] = None

        # set to None if genres (nullable) is None
        # and model_fields_set contains the field
        if self.genres is None and "genres" in self.model_fields_set:
            _dict['genres'] = None

        # set to None if clean_name (nullable) is None
        # and model_fields_set contains the field
        if self.clean_name is None and "clean_name" in self.model_fields_set:
            _dict['cleanName'] = None

        # set to None if sort_name (nullable) is None
        # and model_fields_set contains the field
        if self.sort_name is None and "sort_name" in self.model_fields_set:
            _dict['sortName'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ArtistResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "ended": obj.get("ended"),
            "artistName": obj.get("artistName"),
            "foreignArtistId": obj.get("foreignArtistId"),
            "mbId": obj.get("mbId"),
            "tadbId": obj.get("tadbId"),
            "discogsId": obj.get("discogsId"),
            "allMusicId": obj.get("allMusicId"),
            "overview": obj.get("overview"),
            "artistType": obj.get("artistType"),
            "disambiguation": obj.get("disambiguation"),
            "links": [Links.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "nextAlbum": AlbumResource.from_dict(obj["nextAlbum"]) if obj.get("nextAlbum") is not None else None,
            "lastAlbum": AlbumResource.from_dict(obj["lastAlbum"]) if obj.get("lastAlbum") is not None else None,
            "images": [MediaCover.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "members": [Member.from_dict(_item) for _item in obj["members"]] if obj.get("members") is not None else None,
            "remotePoster": obj.get("remotePoster"),
            "path": obj.get("path"),
            "qualityProfileId": obj.get("qualityProfileId"),
            "metadataProfileId": obj.get("metadataProfileId"),
            "monitored": obj.get("monitored"),
            "monitorNewItems": obj.get("monitorNewItems"),
            "rootFolderPath": obj.get("rootFolderPath"),
            "folder": obj.get("folder"),
            "genres": obj.get("genres"),
            "cleanName": obj.get("cleanName"),
            "sortName": obj.get("sortName"),
            "tags": obj.get("tags"),
            "added": obj.get("added"),
            "addOptions": AddArtistOptions.from_dict(obj["addOptions"]) if obj.get("addOptions") is not None else None,
            "ratings": Ratings.from_dict(obj["ratings"]) if obj.get("ratings") is not None else None,
            "statistics": ArtistStatisticsResource.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None
        })
        return _obj

from lidarr.models.album_resource import AlbumResource
# TODO: Rewrite to not use raise_errors
ArtistResource.model_rebuild(raise_errors=False)

