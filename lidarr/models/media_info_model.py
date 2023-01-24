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


from typing import Optional
from pydantic import BaseModel

class MediaInfoModel(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    audio_format: Optional[str]
    audio_bitrate: Optional[int]
    audio_channels: Optional[int]
    audio_bits: Optional[int]
    audio_sample_rate: Optional[int]
    __properties = ["audioFormat", "audioBitrate", "audioChannels", "audioBits", "audioSampleRate"]

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
    def from_json(cls, json_str: str) -> MediaInfoModel:
        """Create an instance of MediaInfoModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if audio_format (nullable) is None
        if self.audio_format is None:
            _dict['audioFormat'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MediaInfoModel:
        """Create an instance of MediaInfoModel from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MediaInfoModel.parse_obj(obj)

        _obj = MediaInfoModel.parse_obj({
            "audio_format": obj.get("audioFormat"),
            "audio_bitrate": obj.get("audioBitrate"),
            "audio_channels": obj.get("audioChannels"),
            "audio_bits": obj.get("audioBits"),
            "audio_sample_rate": obj.get("audioSampleRate")
        })
        return _obj

