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



from pydantic import BaseModel

class MediaInfoResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    audio_channels: Optional[float]
    audio_bit_rate: Optional[str]
    audio_codec: Optional[str]
    audio_bits: Optional[str]
    audio_sample_rate: Optional[str]
    __properties = ["id", "audioChannels", "audioBitRate", "audioCodec", "audioBits", "audioSampleRate"]

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
    def from_json(cls, json_str: str) -> MediaInfoResource:
        """Create an instance of MediaInfoResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if audio_bit_rate (nullable) is None
        if self.audio_bit_rate is None:
            _dict['audioBitRate'] = None

        # set to None if audio_codec (nullable) is None
        if self.audio_codec is None:
            _dict['audioCodec'] = None

        # set to None if audio_bits (nullable) is None
        if self.audio_bits is None:
            _dict['audioBits'] = None

        # set to None if audio_sample_rate (nullable) is None
        if self.audio_sample_rate is None:
            _dict['audioSampleRate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MediaInfoResource:
        """Create an instance of MediaInfoResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MediaInfoResource.parse_obj(obj)

        _obj = MediaInfoResource.parse_obj({
            "id": obj.get("id"),
            "audio_channels": obj.get("audioChannels"),
            "audio_bit_rate": obj.get("audioBitRate"),
            "audio_codec": obj.get("audioCodec"),
            "audio_bits": obj.get("audioBits"),
            "audio_sample_rate": obj.get("audioSampleRate")
        })
        return _obj

