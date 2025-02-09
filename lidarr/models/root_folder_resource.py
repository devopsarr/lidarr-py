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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.monitor_types import MonitorTypes
from lidarr.models.new_item_monitor_types import NewItemMonitorTypes
from typing import Optional, Set
from typing_extensions import Self

class RootFolderResource(BaseModel):
    """
    RootFolderResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    default_metadata_profile_id: Optional[StrictInt] = Field(default=None, alias="defaultMetadataProfileId")
    default_quality_profile_id: Optional[StrictInt] = Field(default=None, alias="defaultQualityProfileId")
    default_monitor_option: Optional[MonitorTypes] = Field(default=None, alias="defaultMonitorOption")
    default_new_item_monitor_option: Optional[NewItemMonitorTypes] = Field(default=None, alias="defaultNewItemMonitorOption")
    default_tags: Optional[List[StrictInt]] = Field(default=None, alias="defaultTags")
    accessible: Optional[StrictBool] = None
    free_space: Optional[StrictInt] = Field(default=None, alias="freeSpace")
    total_space: Optional[StrictInt] = Field(default=None, alias="totalSpace")
    __properties: ClassVar[List[str]] = ["id", "name", "path", "defaultMetadataProfileId", "defaultQualityProfileId", "defaultMonitorOption", "defaultNewItemMonitorOption", "defaultTags", "accessible", "freeSpace", "totalSpace"]

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
        """Create an instance of RootFolderResource from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if default_tags (nullable) is None
        # and model_fields_set contains the field
        if self.default_tags is None and "default_tags" in self.model_fields_set:
            _dict['defaultTags'] = None

        # set to None if free_space (nullable) is None
        # and model_fields_set contains the field
        if self.free_space is None and "free_space" in self.model_fields_set:
            _dict['freeSpace'] = None

        # set to None if total_space (nullable) is None
        # and model_fields_set contains the field
        if self.total_space is None and "total_space" in self.model_fields_set:
            _dict['totalSpace'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RootFolderResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "defaultMetadataProfileId": obj.get("defaultMetadataProfileId"),
            "defaultQualityProfileId": obj.get("defaultQualityProfileId"),
            "defaultMonitorOption": obj.get("defaultMonitorOption"),
            "defaultNewItemMonitorOption": obj.get("defaultNewItemMonitorOption"),
            "defaultTags": obj.get("defaultTags"),
            "accessible": obj.get("accessible"),
            "freeSpace": obj.get("freeSpace"),
            "totalSpace": obj.get("totalSpace")
        })
        return _obj


