# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.5.3.4341
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.album_resource import AlbumResource
from typing import Optional, Set
from typing_extensions import Self

class AlbumStudioArtistResource(BaseModel):
    """
    AlbumStudioArtistResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    monitored: Optional[StrictBool] = None
    albums: Optional[List[AlbumResource]] = None
    __properties: ClassVar[List[str]] = ["id", "monitored", "albums"]

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
        """Create an instance of AlbumStudioArtistResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in albums (list)
        _items = []
        if self.albums:
            for _item_albums in self.albums:
                if _item_albums:
                    _items.append(_item_albums.to_dict())
            _dict['albums'] = _items
        # set to None if monitored (nullable) is None
        # and model_fields_set contains the field
        if self.monitored is None and "monitored" in self.model_fields_set:
            _dict['monitored'] = None

        # set to None if albums (nullable) is None
        # and model_fields_set contains the field
        if self.albums is None and "albums" in self.model_fields_set:
            _dict['albums'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlbumStudioArtistResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "monitored": obj.get("monitored"),
            "albums": [AlbumResource.from_dict(_item) for _item in obj["albums"]] if obj.get("albums") is not None else None
        })
        return _obj


