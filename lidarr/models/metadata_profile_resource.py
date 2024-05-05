# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.2.5.4141
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.profile_primary_album_type_item_resource import ProfilePrimaryAlbumTypeItemResource
from lidarr.models.profile_release_status_item_resource import ProfileReleaseStatusItemResource
from lidarr.models.profile_secondary_album_type_item_resource import ProfileSecondaryAlbumTypeItemResource
from typing import Optional, Set
from typing_extensions import Self

class MetadataProfileResource(BaseModel):
    """
    MetadataProfileResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    primary_album_types: Optional[List[ProfilePrimaryAlbumTypeItemResource]] = Field(default=None, alias="primaryAlbumTypes")
    secondary_album_types: Optional[List[ProfileSecondaryAlbumTypeItemResource]] = Field(default=None, alias="secondaryAlbumTypes")
    release_statuses: Optional[List[ProfileReleaseStatusItemResource]] = Field(default=None, alias="releaseStatuses")
    __properties: ClassVar[List[str]] = ["id", "name", "primaryAlbumTypes", "secondaryAlbumTypes", "releaseStatuses"]

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
        """Create an instance of MetadataProfileResource from a JSON string"""
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
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if primary_album_types (nullable) is None
        # and model_fields_set contains the field
        if self.primary_album_types is None and "primary_album_types" in self.model_fields_set:
            _dict['primaryAlbumTypes'] = None

        # set to None if secondary_album_types (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_album_types is None and "secondary_album_types" in self.model_fields_set:
            _dict['secondaryAlbumTypes'] = None

        # set to None if release_statuses (nullable) is None
        # and model_fields_set contains the field
        if self.release_statuses is None and "release_statuses" in self.model_fields_set:
            _dict['releaseStatuses'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetadataProfileResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "primaryAlbumTypes": [ProfilePrimaryAlbumTypeItemResource.from_dict(_item) for _item in obj["primaryAlbumTypes"]] if obj.get("primaryAlbumTypes") is not None else None,
            "secondaryAlbumTypes": [ProfileSecondaryAlbumTypeItemResource.from_dict(_item) for _item in obj["secondaryAlbumTypes"]] if obj.get("secondaryAlbumTypes") is not None else None,
            "releaseStatuses": [ProfileReleaseStatusItemResource.from_dict(_item) for _item in obj["releaseStatuses"]] if obj.get("releaseStatuses") is not None else None
        })
        return _obj


