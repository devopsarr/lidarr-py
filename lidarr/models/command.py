# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.8.2.4493
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, Optional
from lidarr.models.command_trigger import CommandTrigger
from typing import Optional, Set
from typing_extensions import Self

class Command(BaseModel):
    """
    Command
    """ # noqa: E501
    send_updates_to_client: Optional[StrictBool] = Field(default=None, alias="sendUpdatesToClient")
    update_scheduled_task: Optional[StrictBool] = Field(default=None, alias="updateScheduledTask")
    completion_message: Optional[StrictStr] = Field(default=None, alias="completionMessage")
    requires_disk_access: Optional[StrictBool] = Field(default=None, alias="requiresDiskAccess")
    is_exclusive: Optional[StrictBool] = Field(default=None, alias="isExclusive")
    is_type_exclusive: Optional[StrictBool] = Field(default=None, alias="isTypeExclusive")
    is_long_running: Optional[StrictBool] = Field(default=None, alias="isLongRunning")
    name: Optional[StrictStr] = None
    last_execution_time: Optional[datetime] = Field(default=None, alias="lastExecutionTime")
    last_start_time: Optional[datetime] = Field(default=None, alias="lastStartTime")
    trigger: Optional[CommandTrigger] = None
    suppress_messages: Optional[StrictBool] = Field(default=None, alias="suppressMessages")
    client_user_agent: Optional[StrictStr] = Field(default=None, alias="clientUserAgent")
    __properties: ClassVar[List[str]] = ["sendUpdatesToClient", "updateScheduledTask", "completionMessage", "requiresDiskAccess", "isExclusive", "isTypeExclusive", "isLongRunning", "name", "lastExecutionTime", "lastStartTime", "trigger", "suppressMessages", "clientUserAgent"]

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
        """Create an instance of Command from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "update_scheduled_task",
            "completion_message",
            "requires_disk_access",
            "is_exclusive",
            "is_type_exclusive",
            "is_long_running",
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if completion_message (nullable) is None
        # and model_fields_set contains the field
        if self.completion_message is None and "completion_message" in self.model_fields_set:
            _dict['completionMessage'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if last_execution_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_execution_time is None and "last_execution_time" in self.model_fields_set:
            _dict['lastExecutionTime'] = None

        # set to None if last_start_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_start_time is None and "last_start_time" in self.model_fields_set:
            _dict['lastStartTime'] = None

        # set to None if client_user_agent (nullable) is None
        # and model_fields_set contains the field
        if self.client_user_agent is None and "client_user_agent" in self.model_fields_set:
            _dict['clientUserAgent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Command from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sendUpdatesToClient": obj.get("sendUpdatesToClient"),
            "updateScheduledTask": obj.get("updateScheduledTask"),
            "completionMessage": obj.get("completionMessage"),
            "requiresDiskAccess": obj.get("requiresDiskAccess"),
            "isExclusive": obj.get("isExclusive"),
            "isTypeExclusive": obj.get("isTypeExclusive"),
            "isLongRunning": obj.get("isLongRunning"),
            "name": obj.get("name"),
            "lastExecutionTime": obj.get("lastExecutionTime"),
            "lastStartTime": obj.get("lastStartTime"),
            "trigger": obj.get("trigger"),
            "suppressMessages": obj.get("suppressMessages"),
            "clientUserAgent": obj.get("clientUserAgent")
        })
        return _obj


