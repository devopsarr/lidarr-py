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


from typing import Any, List, Optional
from pydantic import BaseModel
from lidarr.models.select_option import SelectOption

class Field(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    order: Optional[int]
    name: Optional[str]
    label: Optional[str]
    unit: Optional[str]
    help_text: Optional[str]
    help_text_warning: Optional[str]
    help_link: Optional[str]
    value: Optional[object]
    type: Optional[str]
    advanced: Optional[bool]
    select_options: Optional[List]
    select_options_provider_action: Optional[str]
    section: Optional[str]
    hidden: Optional[str]
    placeholder: Optional[str]
    __properties = ["order", "name", "label", "unit", "helpText", "helpTextWarning", "helpLink", "value", "type", "advanced", "selectOptions", "selectOptionsProviderAction", "section", "hidden", "placeholder"]

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
    def from_json(cls, json_str: str) -> Field:
        """Create an instance of Field from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in select_options (list)
        _items = []
        if self.select_options:
            for _item in self.select_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['selectOptions'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if label (nullable) is None
        if self.label is None:
            _dict['label'] = None

        # set to None if unit (nullable) is None
        if self.unit is None:
            _dict['unit'] = None

        # set to None if help_text (nullable) is None
        if self.help_text is None:
            _dict['helpText'] = None

        # set to None if help_text_warning (nullable) is None
        if self.help_text_warning is None:
            _dict['helpTextWarning'] = None

        # set to None if help_link (nullable) is None
        if self.help_link is None:
            _dict['helpLink'] = None

        # set to None if value (nullable) is None
        if self.value is None:
            _dict['value'] = None

        # set to None if type (nullable) is None
        if self.type is None:
            _dict['type'] = None

        # set to None if select_options (nullable) is None
        if self.select_options is None:
            _dict['selectOptions'] = None

        # set to None if select_options_provider_action (nullable) is None
        if self.select_options_provider_action is None:
            _dict['selectOptionsProviderAction'] = None

        # set to None if section (nullable) is None
        if self.section is None:
            _dict['section'] = None

        # set to None if hidden (nullable) is None
        if self.hidden is None:
            _dict['hidden'] = None

        # set to None if placeholder (nullable) is None
        if self.placeholder is None:
            _dict['placeholder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Field:
        """Create an instance of Field from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Field.parse_obj(obj)

        _obj = Field.parse_obj({
            "order": obj.get("order"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "unit": obj.get("unit"),
            "help_text": obj.get("helpText"),
            "help_text_warning": obj.get("helpTextWarning"),
            "help_link": obj.get("helpLink"),
            "value": obj.get("value"),
            "type": obj.get("type"),
            "advanced": obj.get("advanced"),
            "select_options": [SelectOption.from_dict(_item) for _item in obj.get("selectOptions")] if obj.get("selectOptions") is not None else None,
            "select_options_provider_action": obj.get("selectOptionsProviderAction"),
            "section": obj.get("section"),
            "hidden": obj.get("hidden"),
            "placeholder": obj.get("placeholder")
        })
        return _obj

