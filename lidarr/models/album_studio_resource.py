# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.7.1.4417
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.album_studio_artist_resource import AlbumStudioArtistResource
from lidarr.models.monitoring_options import MonitoringOptions
from lidarr.models.new_item_monitor_types import NewItemMonitorTypes
from typing import Optional, Set
from typing_extensions import Self

class AlbumStudioResource(BaseModel):
    """
    AlbumStudioResource
    """ # noqa: E501
    artist: Optional[List[AlbumStudioArtistResource]] = None
    monitoring_options: Optional[MonitoringOptions] = Field(default=None, alias="monitoringOptions")
    monitor_new_items: Optional[NewItemMonitorTypes] = Field(default=None, alias="monitorNewItems")
    __properties: ClassVar[List[str]] = ["artist", "monitoringOptions", "monitorNewItems"]

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
        """Create an instance of AlbumStudioResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in artist (list)
        _items = []
        if self.artist:
            for _item_artist in self.artist:
                if _item_artist:
                    _items.append(_item_artist.to_dict())
            _dict['artist'] = _items
        # override the default output from pydantic by calling `to_dict()` of monitoring_options
        if self.monitoring_options:
            _dict['monitoringOptions'] = self.monitoring_options.to_dict()
        # set to None if artist (nullable) is None
        # and model_fields_set contains the field
        if self.artist is None and "artist" in self.model_fields_set:
            _dict['artist'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlbumStudioResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "artist": [AlbumStudioArtistResource.from_dict(_item) for _item in obj["artist"]] if obj.get("artist") is not None else None,
            "monitoringOptions": MonitoringOptions.from_dict(obj["monitoringOptions"]) if obj.get("monitoringOptions") is not None else None,
            "monitorNewItems": obj.get("monitorNewItems")
        })
        return _obj


