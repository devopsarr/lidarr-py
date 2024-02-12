# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ArtistStatusType(str, Enum):
    """
    ArtistStatusType
    """

    """
    allowed enum values
    """
    CONTINUING = 'continuing'
    ENDED = 'ended'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ArtistStatusType from a JSON string"""
        return cls(json.loads(json_str))


