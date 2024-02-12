# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, Optional
from lidarr.models.media_cover_types import MediaCoverTypes
from typing import Optional, Set
from typing_extensions import Self

class MediaCover(BaseModel):
    """
    MediaCover
    """ # noqa: E501
    url: Optional[StrictStr] = None
    cover_type: Optional[MediaCoverTypes] = Field(default=None, alias="coverType")
    extension: Optional[StrictStr] = None
    remote_url: Optional[StrictStr] = Field(default=None, alias="remoteUrl")
    __properties: ClassVar[List[str]] = ["url", "coverType", "extension", "remoteUrl"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MediaCover from a JSON string"""
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
            "extension",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if extension (nullable) is None
        # and model_fields_set contains the field
        if self.extension is None and "extension" in self.model_fields_set:
            _dict['extension'] = None

        # set to None if remote_url (nullable) is None
        # and model_fields_set contains the field
        if self.remote_url is None and "remote_url" in self.model_fields_set:
            _dict['remoteUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaCover from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "coverType": obj.get("coverType"),
            "extension": obj.get("extension"),
            "remoteUrl": obj.get("remoteUrl")
        })
        return _obj


