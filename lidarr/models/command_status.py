# coding: utf-8

"""
    Lidarr

    Lidarr API docs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class CommandStatus(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
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

