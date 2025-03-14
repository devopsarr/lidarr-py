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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.quality_model import QualityModel
from lidarr.models.rejection import Rejection
from lidarr.models.track_resource import TrackResource
from typing import Optional, Set
from typing_extensions import Self

class ManualImportUpdateResource(BaseModel):
    """
    ManualImportUpdateResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    path: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    artist_id: Optional[StrictInt] = Field(default=None, alias="artistId")
    album_id: Optional[StrictInt] = Field(default=None, alias="albumId")
    album_release_id: Optional[StrictInt] = Field(default=None, alias="albumReleaseId")
    tracks: Optional[List[TrackResource]] = None
    track_ids: Optional[List[StrictInt]] = Field(default=None, alias="trackIds")
    quality: Optional[QualityModel] = None
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    indexer_flags: Optional[StrictInt] = Field(default=None, alias="indexerFlags")
    download_id: Optional[StrictStr] = Field(default=None, alias="downloadId")
    additional_file: Optional[StrictBool] = Field(default=None, alias="additionalFile")
    replace_existing_files: Optional[StrictBool] = Field(default=None, alias="replaceExistingFiles")
    disable_release_switching: Optional[StrictBool] = Field(default=None, alias="disableReleaseSwitching")
    rejections: Optional[List[Rejection]] = None
    __properties: ClassVar[List[str]] = ["id", "path", "name", "artistId", "albumId", "albumReleaseId", "tracks", "trackIds", "quality", "releaseGroup", "indexerFlags", "downloadId", "additionalFile", "replaceExistingFiles", "disableReleaseSwitching", "rejections"]

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
        """Create an instance of ManualImportUpdateResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tracks (list)
        _items = []
        if self.tracks:
            for _item_tracks in self.tracks:
                if _item_tracks:
                    _items.append(_item_tracks.to_dict())
            _dict['tracks'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rejections (list)
        _items = []
        if self.rejections:
            for _item_rejections in self.rejections:
                if _item_rejections:
                    _items.append(_item_rejections.to_dict())
            _dict['rejections'] = _items
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if artist_id (nullable) is None
        # and model_fields_set contains the field
        if self.artist_id is None and "artist_id" in self.model_fields_set:
            _dict['artistId'] = None

        # set to None if album_id (nullable) is None
        # and model_fields_set contains the field
        if self.album_id is None and "album_id" in self.model_fields_set:
            _dict['albumId'] = None

        # set to None if album_release_id (nullable) is None
        # and model_fields_set contains the field
        if self.album_release_id is None and "album_release_id" in self.model_fields_set:
            _dict['albumReleaseId'] = None

        # set to None if tracks (nullable) is None
        # and model_fields_set contains the field
        if self.tracks is None and "tracks" in self.model_fields_set:
            _dict['tracks'] = None

        # set to None if track_ids (nullable) is None
        # and model_fields_set contains the field
        if self.track_ids is None and "track_ids" in self.model_fields_set:
            _dict['trackIds'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if download_id (nullable) is None
        # and model_fields_set contains the field
        if self.download_id is None and "download_id" in self.model_fields_set:
            _dict['downloadId'] = None

        # set to None if rejections (nullable) is None
        # and model_fields_set contains the field
        if self.rejections is None and "rejections" in self.model_fields_set:
            _dict['rejections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManualImportUpdateResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "name": obj.get("name"),
            "artistId": obj.get("artistId"),
            "albumId": obj.get("albumId"),
            "albumReleaseId": obj.get("albumReleaseId"),
            "tracks": [TrackResource.from_dict(_item) for _item in obj["tracks"]] if obj.get("tracks") is not None else None,
            "trackIds": obj.get("trackIds"),
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "releaseGroup": obj.get("releaseGroup"),
            "indexerFlags": obj.get("indexerFlags"),
            "downloadId": obj.get("downloadId"),
            "additionalFile": obj.get("additionalFile"),
            "replaceExistingFiles": obj.get("replaceExistingFiles"),
            "disableReleaseSwitching": obj.get("disableReleaseSwitching"),
            "rejections": [Rejection.from_dict(_item) for _item in obj["rejections"]] if obj.get("rejections") is not None else None
        })
        return _obj


