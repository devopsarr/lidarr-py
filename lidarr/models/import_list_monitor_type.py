# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.7.1.4417
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ImportListMonitorType(str, Enum):
    """
    ImportListMonitorType
    """

    """
    allowed enum values
    """
    NONE = 'none'
    SPECIFICALBUM = 'specificAlbum'
    ENTIREARTIST = 'entireArtist'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ImportListMonitorType from a JSON string"""
        return cls(json.loads(json_str))


