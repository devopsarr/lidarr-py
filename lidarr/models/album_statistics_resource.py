# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.1.7.4030
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AlbumStatisticsResource(BaseModel):
    """
    AlbumStatisticsResource
    """ # noqa: E501
    track_file_count: Optional[StrictInt] = Field(default=None, alias="trackFileCount")
    track_count: Optional[StrictInt] = Field(default=None, alias="trackCount")
    total_track_count: Optional[StrictInt] = Field(default=None, alias="totalTrackCount")
    size_on_disk: Optional[StrictInt] = Field(default=None, alias="sizeOnDisk")
    percent_of_tracks: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="percentOfTracks")
    __properties: ClassVar[List[str]] = ["trackFileCount", "trackCount", "totalTrackCount", "sizeOnDisk", "percentOfTracks"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AlbumStatisticsResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "percent_of_tracks",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlbumStatisticsResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "trackFileCount": obj.get("trackFileCount"),
            "trackCount": obj.get("trackCount"),
            "totalTrackCount": obj.get("totalTrackCount"),
            "sizeOnDisk": obj.get("sizeOnDisk"),
            "percentOfTracks": obj.get("percentOfTracks")
        })
        return _obj


