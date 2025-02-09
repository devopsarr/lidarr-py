# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.9.6.4552
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CommandStatus(str, Enum):
    """
    CommandStatus
    """

    """
    allowed enum values
    """
    QUEUED = 'queued'
    STARTED = 'started'
    COMPLETED = 'completed'
    FAILED = 'failed'
    ABORTED = 'aborted'
    CANCELLED = 'cancelled'
    ORPHANED = 'orphaned'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CommandStatus from a JSON string"""
        return cls(json.loads(json_str))


