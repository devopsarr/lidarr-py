# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.5.3.4341
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DownloadProtocol(str, Enum):
    """
    DownloadProtocol
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    USENET = 'usenet'
    TORRENT = 'torrent'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DownloadProtocol from a JSON string"""
        return cls(json.loads(json_str))


