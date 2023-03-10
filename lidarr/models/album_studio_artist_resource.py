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
from lidarr.models.album_resource import AlbumResource

class AlbumStudioArtistResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    monitored: Optional[bool]
    albums: Optional[List]
    __properties = ["id", "monitored", "albums"]

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
    def from_json(cls, json_str: str) -> AlbumStudioArtistResource:
        """Create an instance of AlbumStudioArtistResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in albums (list)
        _items = []
        if self.albums:
            for _item in self.albums:
                if _item:
                    _items.append(_item.to_dict())
            _dict['albums'] = _items
        # set to None if monitored (nullable) is None
        if self.monitored is None:
            _dict['monitored'] = None

        # set to None if albums (nullable) is None
        if self.albums is None:
            _dict['albums'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlbumStudioArtistResource:
        """Create an instance of AlbumStudioArtistResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AlbumStudioArtistResource.parse_obj(obj)

        _obj = AlbumStudioArtistResource.parse_obj({
            "id": obj.get("id"),
            "monitored": obj.get("monitored"),
            "albums": [AlbumResource.from_dict(_item) for _item in obj.get("albums")] if obj.get("albums") is not None else None
        })
        return _obj

