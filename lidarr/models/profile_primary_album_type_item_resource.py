# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.6.4.4402
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, Optional
from lidarr.models.primary_album_type import PrimaryAlbumType
from typing import Optional, Set
from typing_extensions import Self

class ProfilePrimaryAlbumTypeItemResource(BaseModel):
    """
    ProfilePrimaryAlbumTypeItemResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    album_type: Optional[PrimaryAlbumType] = Field(default=None, alias="albumType")
    allowed: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "albumType", "allowed"]

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
        """Create an instance of ProfilePrimaryAlbumTypeItemResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of album_type
        if self.album_type:
            _dict['albumType'] = self.album_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfilePrimaryAlbumTypeItemResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "albumType": PrimaryAlbumType.from_dict(obj["albumType"]) if obj.get("albumType") is not None else None,
            "allowed": obj.get("allowed")
        })
        return _obj


