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
from lidarr.models.profile_primary_album_type_item import ProfilePrimaryAlbumTypeItem
from lidarr.models.profile_release_status_item import ProfileReleaseStatusItem
from lidarr.models.profile_secondary_album_type_item import ProfileSecondaryAlbumTypeItem

class MetadataProfile(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    primary_album_types: Optional[List]
    secondary_album_types: Optional[List]
    release_statuses: Optional[List]
    __properties = ["id", "name", "primaryAlbumTypes", "secondaryAlbumTypes", "releaseStatuses"]

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
    def from_json(cls, json_str: str) -> MetadataProfile:
        """Create an instance of MetadataProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in primary_album_types (list)
        _items = []
        if self.primary_album_types:
            for _item in self.primary_album_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['primaryAlbumTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in secondary_album_types (list)
        _items = []
        if self.secondary_album_types:
            for _item in self.secondary_album_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['secondaryAlbumTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in release_statuses (list)
        _items = []
        if self.release_statuses:
            for _item in self.release_statuses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['releaseStatuses'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if primary_album_types (nullable) is None
        if self.primary_album_types is None:
            _dict['primaryAlbumTypes'] = None

        # set to None if secondary_album_types (nullable) is None
        if self.secondary_album_types is None:
            _dict['secondaryAlbumTypes'] = None

        # set to None if release_statuses (nullable) is None
        if self.release_statuses is None:
            _dict['releaseStatuses'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MetadataProfile:
        """Create an instance of MetadataProfile from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MetadataProfile.parse_obj(obj)

        _obj = MetadataProfile.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "primary_album_types": [ProfilePrimaryAlbumTypeItem.from_dict(_item) for _item in obj.get("primaryAlbumTypes")] if obj.get("primaryAlbumTypes") is not None else None,
            "secondary_album_types": [ProfileSecondaryAlbumTypeItem.from_dict(_item) for _item in obj.get("secondaryAlbumTypes")] if obj.get("secondaryAlbumTypes") is not None else None,
            "release_statuses": [ProfileReleaseStatusItem.from_dict(_item) for _item in obj.get("releaseStatuses")] if obj.get("releaseStatuses") is not None else None
        })
        return _obj

