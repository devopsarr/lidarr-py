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
from lidarr.models.health_check_result import HealthCheckResult
from lidarr.models.http_uri import HttpUri

class HealthResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    source: Optional[str]
    type: Optional[HealthCheckResult]
    message: Optional[str]
    wiki_url: Optional[HttpUri]
    __properties = ["id", "source", "type", "message", "wikiUrl"]

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
    def from_json(cls, json_str: str) -> HealthResource:
        """Create an instance of HealthResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of wiki_url
        if self.wiki_url:
            _dict['wikiUrl'] = self.wiki_url.to_dict()
        # set to None if source (nullable) is None
        if self.source is None:
            _dict['source'] = None

        # set to None if message (nullable) is None
        if self.message is None:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HealthResource:
        """Create an instance of HealthResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HealthResource.parse_obj(obj)

        _obj = HealthResource.parse_obj({
            "id": obj.get("id"),
            "source": obj.get("source"),
            "type": obj.get("type"),
            "message": obj.get("message"),
            "wiki_url": HttpUri.from_dict(obj.get("wikiUrl")) if obj.get("wikiUrl") is not None else None
        })
        return _obj

