# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.1.7.4030
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DatabaseType(str, Enum):
    """
    DatabaseType
    """

    """
    allowed enum values
    """
    SQLITE = 'sqLite'
    POSTGRESQL = 'postgreSQL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DatabaseType from a JSON string"""
        return cls(json.loads(json_str))


