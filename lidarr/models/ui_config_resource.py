# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.2.5.4141
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class UiConfigResource(BaseModel):
    """
    UiConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    first_day_of_week: Optional[StrictInt] = Field(default=None, alias="firstDayOfWeek")
    calendar_week_column_header: Optional[StrictStr] = Field(default=None, alias="calendarWeekColumnHeader")
    short_date_format: Optional[StrictStr] = Field(default=None, alias="shortDateFormat")
    long_date_format: Optional[StrictStr] = Field(default=None, alias="longDateFormat")
    time_format: Optional[StrictStr] = Field(default=None, alias="timeFormat")
    show_relative_dates: Optional[StrictBool] = Field(default=None, alias="showRelativeDates")
    enable_color_impaired_mode: Optional[StrictBool] = Field(default=None, alias="enableColorImpairedMode")
    ui_language: Optional[StrictInt] = Field(default=None, alias="uiLanguage")
    expand_album_by_default: Optional[StrictBool] = Field(default=None, alias="expandAlbumByDefault")
    expand_single_by_default: Optional[StrictBool] = Field(default=None, alias="expandSingleByDefault")
    expand_epby_default: Optional[StrictBool] = Field(default=None, alias="expandEPByDefault")
    expand_broadcast_by_default: Optional[StrictBool] = Field(default=None, alias="expandBroadcastByDefault")
    expand_other_by_default: Optional[StrictBool] = Field(default=None, alias="expandOtherByDefault")
    theme: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "firstDayOfWeek", "calendarWeekColumnHeader", "shortDateFormat", "longDateFormat", "timeFormat", "showRelativeDates", "enableColorImpairedMode", "uiLanguage", "expandAlbumByDefault", "expandSingleByDefault", "expandEPByDefault", "expandBroadcastByDefault", "expandOtherByDefault", "theme"]

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
        """Create an instance of UiConfigResource from a JSON string"""
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
        # set to None if calendar_week_column_header (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_week_column_header is None and "calendar_week_column_header" in self.model_fields_set:
            _dict['calendarWeekColumnHeader'] = None

        # set to None if short_date_format (nullable) is None
        # and model_fields_set contains the field
        if self.short_date_format is None and "short_date_format" in self.model_fields_set:
            _dict['shortDateFormat'] = None

        # set to None if long_date_format (nullable) is None
        # and model_fields_set contains the field
        if self.long_date_format is None and "long_date_format" in self.model_fields_set:
            _dict['longDateFormat'] = None

        # set to None if time_format (nullable) is None
        # and model_fields_set contains the field
        if self.time_format is None and "time_format" in self.model_fields_set:
            _dict['timeFormat'] = None

        # set to None if theme (nullable) is None
        # and model_fields_set contains the field
        if self.theme is None and "theme" in self.model_fields_set:
            _dict['theme'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UiConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "firstDayOfWeek": obj.get("firstDayOfWeek"),
            "calendarWeekColumnHeader": obj.get("calendarWeekColumnHeader"),
            "shortDateFormat": obj.get("shortDateFormat"),
            "longDateFormat": obj.get("longDateFormat"),
            "timeFormat": obj.get("timeFormat"),
            "showRelativeDates": obj.get("showRelativeDates"),
            "enableColorImpairedMode": obj.get("enableColorImpairedMode"),
            "uiLanguage": obj.get("uiLanguage"),
            "expandAlbumByDefault": obj.get("expandAlbumByDefault"),
            "expandSingleByDefault": obj.get("expandSingleByDefault"),
            "expandEPByDefault": obj.get("expandEPByDefault"),
            "expandBroadcastByDefault": obj.get("expandBroadcastByDefault"),
            "expandOtherByDefault": obj.get("expandOtherByDefault"),
            "theme": obj.get("theme")
        })
        return _obj


