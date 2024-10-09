# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.6.4.4402
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TrackedDownloadStatus(str, Enum):
    """
    TrackedDownloadStatus
    """

    """
    allowed enum values
    """
    OK = 'ok'
    WARNING = 'warning'
    ERROR = 'error'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TrackedDownloadStatus from a JSON string"""
        return cls(json.loads(json_str))


