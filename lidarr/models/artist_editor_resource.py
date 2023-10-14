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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from lidarr.models.apply_tags import ApplyTags
from lidarr.models.new_item_monitor_types import NewItemMonitorTypes

class ArtistEditorResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    artist_ids: Optional[List]
    monitored: Optional[bool]
    monitor_new_items: Optional[NewItemMonitorTypes]
    quality_profile_id: Optional[int]
    metadata_profile_id: Optional[int]
    root_folder_path: Optional[str]
    tags: Optional[List]
    apply_tags: Optional[ApplyTags]
    move_files: Optional[bool]
    delete_files: Optional[bool]
    __properties = ["artistIds", "monitored", "monitorNewItems", "qualityProfileId", "metadataProfileId", "rootFolderPath", "tags", "applyTags", "moveFiles", "deleteFiles"]

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
    def from_json(cls, json_str: str) -> ArtistEditorResource:
        """Create an instance of ArtistEditorResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if artist_ids (nullable) is None
        if self.artist_ids is None:
            _dict['artistIds'] = None

        # set to None if monitored (nullable) is None
        if self.monitored is None:
            _dict['monitored'] = None

        # set to None if quality_profile_id (nullable) is None
        if self.quality_profile_id is None:
            _dict['qualityProfileId'] = None

        # set to None if metadata_profile_id (nullable) is None
        if self.metadata_profile_id is None:
            _dict['metadataProfileId'] = None

        # set to None if root_folder_path (nullable) is None
        if self.root_folder_path is None:
            _dict['rootFolderPath'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ArtistEditorResource:
        """Create an instance of ArtistEditorResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ArtistEditorResource.parse_obj(obj)

        _obj = ArtistEditorResource.parse_obj({
            "artist_ids": obj.get("artistIds"),
            "monitored": obj.get("monitored"),
            "monitor_new_items": obj.get("monitorNewItems"),
            "quality_profile_id": obj.get("qualityProfileId"),
            "metadata_profile_id": obj.get("metadataProfileId"),
            "root_folder_path": obj.get("rootFolderPath"),
            "tags": obj.get("tags"),
            "apply_tags": obj.get("applyTags"),
            "move_files": obj.get("moveFiles"),
            "delete_files": obj.get("deleteFiles")
        })
        return _obj

