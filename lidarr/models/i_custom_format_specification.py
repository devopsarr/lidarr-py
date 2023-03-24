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

class ICustomFormatSpecification(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    order: Optional[int]
    info_link: Optional[str]
    implementation_name: Optional[str]
    name: Optional[str]
    negate: Optional[bool]
    required: Optional[bool]
    __properties = ["order", "infoLink", "implementationName", "name", "negate", "required"]

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
    def from_json(cls, json_str: str) -> ICustomFormatSpecification:
        """Create an instance of ICustomFormatSpecification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "order",
                            "info_link",
                            "implementation_name",
                          },
                          exclude_none=True)
        # set to None if info_link (nullable) is None
        if self.info_link is None:
            _dict['infoLink'] = None

        # set to None if implementation_name (nullable) is None
        if self.implementation_name is None:
            _dict['implementationName'] = None

        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ICustomFormatSpecification:
        """Create an instance of ICustomFormatSpecification from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ICustomFormatSpecification.parse_obj(obj)

        _obj = ICustomFormatSpecification.parse_obj({
            "order": obj.get("order"),
            "info_link": obj.get("infoLink"),
            "implementation_name": obj.get("implementationName"),
            "name": obj.get("name"),
            "negate": obj.get("negate"),
            "required": obj.get("required")
        })
        return _obj

