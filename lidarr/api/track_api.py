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

from pydantic import StrictInt

from typing import List, Optional

from lidarr.models.track_resource import TrackResource

from lidarr.api_client import ApiClient
from lidarr.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TrackApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_track_by_id(self, id : StrictInt, **kwargs) -> TrackResource:  # noqa: E501
        """get_track_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_track_by_id(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
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
        :rtype: TrackResource
        """
        kwargs['_return_http_data_only'] = True
        return self.get_track_by_id_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_track_by_id_with_http_info(self, id : StrictInt, **kwargs):  # noqa: E501
        """get_track_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_track_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
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
        :rtype: tuple(TrackResource, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
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
                    " to method get_track_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Api-Key', 'apikey']  # noqa: E501

        _response_types_map = {
            '200': "TrackResource",
        }

        return self.api_client.call_api(
            '/api/v1/track/{id}', 'GET',
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

    @validate_arguments
    def list_track(self, artist_id : Optional[StrictInt] = None, album_id : Optional[StrictInt] = None, album_release_id : Optional[StrictInt] = None, track_ids : Optional[List[StrictInt]] = None, **kwargs) -> List[TrackResource]:  # noqa: E501
        """list_track  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_track(artist_id, album_id, album_release_id, track_ids, async_req=True)
        >>> result = thread.get()

        :param artist_id:
        :type artist_id: int
        :param album_id:
        :type album_id: int
        :param album_release_id:
        :type album_release_id: int
        :param track_ids:
        :type track_ids: List[int]
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
        :rtype: List[TrackResource]
        """
        kwargs['_return_http_data_only'] = True
        return self.list_track_with_http_info(artist_id, album_id, album_release_id, track_ids, **kwargs)  # noqa: E501

    @validate_arguments
    def list_track_with_http_info(self, artist_id : Optional[StrictInt] = None, album_id : Optional[StrictInt] = None, album_release_id : Optional[StrictInt] = None, track_ids : Optional[List[StrictInt]] = None, **kwargs):  # noqa: E501
        """list_track  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_track_with_http_info(artist_id, album_id, album_release_id, track_ids, async_req=True)
        >>> result = thread.get()

        :param artist_id:
        :type artist_id: int
        :param album_id:
        :type album_id: int
        :param album_release_id:
        :type album_release_id: int
        :param track_ids:
        :type track_ids: List[int]
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
        :rtype: tuple(List[TrackResource], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'artist_id',
            'album_id',
            'album_release_id',
            'track_ids'
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
                    " to method list_track" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('artist_id') is not None:  # noqa: E501
            _query_params.append(('artistId', _params['artist_id']))
        if _params.get('album_id') is not None:  # noqa: E501
            _query_params.append(('albumId', _params['album_id']))
        if _params.get('album_release_id') is not None:  # noqa: E501
            _query_params.append(('albumReleaseId', _params['album_release_id']))
        if _params.get('track_ids') is not None:  # noqa: E501
            _query_params.append(('trackIds', _params['track_ids']))
            _collection_formats['trackIds'] = 'multi'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Api-Key', 'apikey']  # noqa: E501

        _response_types_map = {
            '200': "List[TrackResource]",
        }

        return self.api_client.call_api(
            '/api/v1/track', 'GET',
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
