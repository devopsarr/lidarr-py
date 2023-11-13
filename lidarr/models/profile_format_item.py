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


from typing import Any, ClassVar, Dict, Optional
from pydantic import BaseModel
from lidarr.models.custom_format import CustomFormat

class ProfileFormatItem(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    format: Optional[CustomFormat]
    score: Optional[int]
    __properties = ["format", "score"]

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
    def from_json(cls, json_str: str) -> ProfileFormatItem:
        """Create an instance of ProfileFormatItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of format
        if self.format:
            _dict['format'] = self.format.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProfileFormatItem:
        """Create an instance of ProfileFormatItem from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProfileFormatItem.parse_obj(obj)

        _obj = ProfileFormatItem.parse_obj({
            "format": CustomFormat.from_dict(obj.get("format")) if obj.get("format") is not None else None,
            "score": obj.get("score")
        })
        return _obj

