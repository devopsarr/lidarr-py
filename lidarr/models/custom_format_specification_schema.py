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
from lidarr.models.field import Field

class CustomFormatSpecificationSchema(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    implementation: Optional[str]
    implementation_name: Optional[str]
    info_link: Optional[str]
    negate: Optional[bool]
    required: Optional[bool]
    fields: Optional[List]
    presets: Optional[List]
    __properties = ["id", "name", "implementation", "implementationName", "infoLink", "negate", "required", "fields", "presets"]

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
    def from_json(cls, json_str: str) -> CustomFormatSpecificationSchema:
        """Create an instance of CustomFormatSpecificationSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in presets (list)
        _items = []
        if self.presets:
            for _item in self.presets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['presets'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if implementation (nullable) is None
        if self.implementation is None:
            _dict['implementation'] = None

        # set to None if implementation_name (nullable) is None
        if self.implementation_name is None:
            _dict['implementationName'] = None

        # set to None if info_link (nullable) is None
        if self.info_link is None:
            _dict['infoLink'] = None

        # set to None if fields (nullable) is None
        if self.fields is None:
            _dict['fields'] = None

        # set to None if presets (nullable) is None
        if self.presets is None:
            _dict['presets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomFormatSpecificationSchema:
        """Create an instance of CustomFormatSpecificationSchema from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CustomFormatSpecificationSchema.parse_obj(obj)

        _obj = CustomFormatSpecificationSchema.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "implementation": obj.get("implementation"),
            "implementation_name": obj.get("implementationName"),
            "info_link": obj.get("infoLink"),
            "negate": obj.get("negate"),
            "required": obj.get("required"),
            "fields": [Field.from_dict(_item) for _item in obj.get("fields")] if obj.get("fields") is not None else None,
            "presets": [CustomFormatSpecificationSchema.from_dict(_item) for _item in obj.get("presets")] if obj.get("presets") is not None else None
        })
        return _obj

