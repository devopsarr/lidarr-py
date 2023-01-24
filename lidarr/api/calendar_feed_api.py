# coding: utf-8

"""
    Lidarr

    Lidarr API docs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import StrictBool, StrictInt, StrictStr

from typing import Optional


from lidarr.api_client import ApiClient
from lidarr.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CalendarFeedApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_feed_v1_calendar_lidarr_ics(self, past_days : Optional[StrictInt] = None, future_days : Optional[StrictInt] = None, tag_list : Optional[StrictStr] = None, unmonitored : Optional[StrictBool] = None, **kwargs) -> None:  # noqa: E501
        """get_feed_v1_calendar_lidarr_ics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_feed_v1_calendar_lidarr_ics(past_days, future_days, tag_list, unmonitored, async_req=True)
        >>> result = thread.get()

        :param past_days:
        :type past_days: int
        :param future_days:
        :type future_days: int
        :param tag_list:
        :type tag_list: str
        :param unmonitored:
        :type unmonitored: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.get_feed_v1_calendar_lidarr_ics_with_http_info(past_days, future_days, tag_list, unmonitored, **kwargs)  # noqa: E501

    @validate_arguments
    def get_feed_v1_calendar_lidarr_ics_with_http_info(self, past_days : Optional[StrictInt] = None, future_days : Optional[StrictInt] = None, tag_list : Optional[StrictStr] = None, unmonitored : Optional[StrictBool] = None, **kwargs):  # noqa: E501
        """get_feed_v1_calendar_lidarr_ics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_feed_v1_calendar_lidarr_ics_with_http_info(past_days, future_days, tag_list, unmonitored, async_req=True)
        >>> result = thread.get()

        :param past_days:
        :type past_days: int
        :param future_days:
        :type future_days: int
        :param tag_list:
        :type tag_list: str
        :param unmonitored:
        :type unmonitored: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'past_days',
            'future_days',
            'tag_list',
            'unmonitored'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feed_v1_calendar_lidarr_ics" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('past_days') is not None:  # noqa: E501
            _query_params.append(('pastDays', _params['past_days']))
        if _params.get('future_days') is not None:  # noqa: E501
            _query_params.append(('futureDays', _params['future_days']))
        if _params.get('tag_list') is not None:  # noqa: E501
            _query_params.append(('tagList', _params['tag_list']))
        if _params.get('unmonitored') is not None:  # noqa: E501
            _query_params.append(('unmonitored', _params['unmonitored']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # authentication setting
        _auth_settings = ['X-Api-Key', 'apikey']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/feed/v1/calendar/lidarr.ics', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
