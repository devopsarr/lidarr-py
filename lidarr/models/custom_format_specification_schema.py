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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.field import Field
from typing import Optional, Set
from typing_extensions import Self

class CustomFormatSpecificationSchema(BaseModel):
    """
    CustomFormatSpecificationSchema
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    implementation: Optional[StrictStr] = None
    implementation_name: Optional[StrictStr] = Field(default=None, alias="implementationName")
    info_link: Optional[StrictStr] = Field(default=None, alias="infoLink")
    negate: Optional[StrictBool] = None
    required: Optional[StrictBool] = None
    fields: Optional[List[Field]] = None
    presets: Optional[List[CustomFormatSpecificationSchema]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "implementation", "implementationName", "infoLink", "negate", "required", "fields", "presets"]

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
        """Create an instance of CustomFormatSpecificationSchema from a JSON string"""
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
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if implementation (nullable) is None
        # and model_fields_set contains the field
        if self.implementation is None and "implementation" in self.model_fields_set:
            _dict['implementation'] = None

        # set to None if implementation_name (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_name is None and "implementation_name" in self.model_fields_set:
            _dict['implementationName'] = None

        # set to None if info_link (nullable) is None
        # and model_fields_set contains the field
        if self.info_link is None and "info_link" in self.model_fields_set:
            _dict['infoLink'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        # set to None if presets (nullable) is None
        # and model_fields_set contains the field
        if self.presets is None and "presets" in self.model_fields_set:
            _dict['presets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomFormatSpecificationSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "implementation": obj.get("implementation"),
            "implementationName": obj.get("implementationName"),
            "infoLink": obj.get("infoLink"),
            "negate": obj.get("negate"),
            "required": obj.get("required"),
            "fields": [Field.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "presets": [CustomFormatSpecificationSchema.from_dict(_item) for _item in obj["presets"]] if obj.get("presets") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
CustomFormatSpecificationSchema.model_rebuild(raise_errors=False)

