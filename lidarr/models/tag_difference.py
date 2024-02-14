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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class TagDifference(BaseModel):
    """
    TagDifference
    """ # noqa: E501
    field: Optional[StrictStr] = None
    old_value: Optional[StrictStr] = Field(default=None, alias="oldValue")
    new_value: Optional[StrictStr] = Field(default=None, alias="newValue")
    __properties: ClassVar[List[str]] = ["field", "oldValue", "newValue"]

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
        """Create an instance of TagDifference from a JSON string"""
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
        # set to None if field (nullable) is None
        # and model_fields_set contains the field
        if self.field is None and "field" in self.model_fields_set:
            _dict['field'] = None

        # set to None if old_value (nullable) is None
        # and model_fields_set contains the field
        if self.old_value is None and "old_value" in self.model_fields_set:
            _dict['oldValue'] = None

        # set to None if new_value (nullable) is None
        # and model_fields_set contains the field
        if self.new_value is None and "new_value" in self.model_fields_set:
            _dict['newValue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TagDifference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "field": obj.get("field"),
            "oldValue": obj.get("oldValue"),
            "newValue": obj.get("newValue")
        })
        return _obj


