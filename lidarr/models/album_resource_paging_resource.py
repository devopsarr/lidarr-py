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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from lidarr.models.album_resource import AlbumResource
from lidarr.models.sort_direction import SortDirection

class AlbumResourcePagingResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    page: Optional[int]
    page_size: Optional[int]
    sort_key: Optional[str]
    sort_direction: Optional[SortDirection]
    total_records: Optional[int]
    records: Optional[List]
    __properties = ["page", "pageSize", "sortKey", "sortDirection", "totalRecords", "records"]

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
    def from_json(cls, json_str: str) -> AlbumResourcePagingResource:
        """Create an instance of AlbumResourcePagingResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in records (list)
        _items = []
        if self.records:
            for _item in self.records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['records'] = _items
        # set to None if sort_key (nullable) is None
        if self.sort_key is None:
            _dict['sortKey'] = None

        # set to None if records (nullable) is None
        if self.records is None:
            _dict['records'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlbumResourcePagingResource:
        """Create an instance of AlbumResourcePagingResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AlbumResourcePagingResource.parse_obj(obj)

        _obj = AlbumResourcePagingResource.parse_obj({
            "page": obj.get("page"),
            "page_size": obj.get("pageSize"),
            "sort_key": obj.get("sortKey"),
            "sort_direction": obj.get("sortDirection"),
            "total_records": obj.get("totalRecords"),
            "records": [AlbumResource.from_dict(_item) for _item in obj.get("records")] if obj.get("records") is not None else None
        })
        return _obj

