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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class MediaInfoModel(BaseModel):
    """
    MediaInfoModel
    """ # noqa: E501
    audio_format: Optional[StrictStr] = Field(default=None, alias="audioFormat")
    audio_bitrate: Optional[StrictInt] = Field(default=None, alias="audioBitrate")
    audio_channels: Optional[StrictInt] = Field(default=None, alias="audioChannels")
    audio_bits: Optional[StrictInt] = Field(default=None, alias="audioBits")
    audio_sample_rate: Optional[StrictInt] = Field(default=None, alias="audioSampleRate")
    __properties: ClassVar[List[str]] = ["audioFormat", "audioBitrate", "audioChannels", "audioBits", "audioSampleRate"]

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
        """Create an instance of MediaInfoModel from a JSON string"""
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
        # set to None if audio_format (nullable) is None
        # and model_fields_set contains the field
        if self.audio_format is None and "audio_format" in self.model_fields_set:
            _dict['audioFormat'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaInfoModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "audioFormat": obj.get("audioFormat"),
            "audioBitrate": obj.get("audioBitrate"),
            "audioChannels": obj.get("audioChannels"),
            "audioBits": obj.get("audioBits"),
            "audioSampleRate": obj.get("audioSampleRate")
        })
        return _obj


