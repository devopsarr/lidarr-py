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

from pydantic import StrictBool, StrictInt, StrictStr, conlist

from typing import Optional

from lidarr.models.download_protocol import DownloadProtocol
from lidarr.models.queue_bulk_resource import QueueBulkResource
from lidarr.models.queue_resource_paging_resource import QueueResourcePagingResource
from lidarr.models.sort_direction import SortDirection

from lidarr.api_client import ApiClient
from lidarr.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class QueueApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def delete_queue(self, id : StrictInt, remove_from_client : Optional[StrictBool] = None, blocklist : Optional[StrictBool] = None, skip_redownload : Optional[StrictBool] = None, **kwargs) -> None:  # noqa: E501
        """delete_queue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_queue(id, remove_from_client, blocklist, skip_redownload, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
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
        return self.delete_queue_with_http_info(id, remove_from_client, blocklist, skip_redownload, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_queue_with_http_info(self, id : StrictInt, remove_from_client : Optional[StrictBool] = None, blocklist : Optional[StrictBool] = None, skip_redownload : Optional[StrictBool] = None, **kwargs):  # noqa: E501
        """delete_queue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_queue_with_http_info(id, remove_from_client, blocklist, skip_redownload, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
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
            'id',
            'remove_from_client',
            'blocklist',
            'skip_redownload'
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
                    " to method delete_queue" % _key
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
        if _params.get('remove_from_client') is not None:  # noqa: E501
            _query_params.append(('removeFromClient', _params['remove_from_client']))
        if _params.get('blocklist') is not None:  # noqa: E501
            _query_params.append(('blocklist', _params['blocklist']))
        if _params.get('skip_redownload') is not None:  # noqa: E501
            _query_params.append(('skipRedownload', _params['skip_redownload']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # authentication setting
        _auth_settings = ['apikey', 'X-Api-Key']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/queue/{id}', 'DELETE',
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
    def delete_queue_bulk(self, remove_from_client : Optional[StrictBool] = None, blocklist : Optional[StrictBool] = None, skip_redownload : Optional[StrictBool] = None, queue_bulk_resource : Optional[QueueBulkResource] = None, **kwargs) -> None:  # noqa: E501
        """delete_queue_bulk  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_queue_bulk(remove_from_client, blocklist, skip_redownload, queue_bulk_resource, async_req=True)
        >>> result = thread.get()

        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
        :param queue_bulk_resource:
        :type queue_bulk_resource: QueueBulkResource
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
        return self.delete_queue_bulk_with_http_info(remove_from_client, blocklist, skip_redownload, queue_bulk_resource, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_queue_bulk_with_http_info(self, remove_from_client : Optional[StrictBool] = None, blocklist : Optional[StrictBool] = None, skip_redownload : Optional[StrictBool] = None, queue_bulk_resource : Optional[QueueBulkResource] = None, **kwargs):  # noqa: E501
        """delete_queue_bulk  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_queue_bulk_with_http_info(remove_from_client, blocklist, skip_redownload, queue_bulk_resource, async_req=True)
        >>> result = thread.get()

        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
        :param queue_bulk_resource:
        :type queue_bulk_resource: QueueBulkResource
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
            'remove_from_client',
            'blocklist',
            'skip_redownload',
            'queue_bulk_resource'
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
                    " to method delete_queue_bulk" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('remove_from_client') is not None:  # noqa: E501
            _query_params.append(('removeFromClient', _params['remove_from_client']))
        if _params.get('blocklist') is not None:  # noqa: E501
            _query_params.append(('blocklist', _params['blocklist']))
        if _params.get('skip_redownload') is not None:  # noqa: E501
            _query_params.append(('skipRedownload', _params['skip_redownload']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['queue_bulk_resource']:
            _body_params = _params['queue_bulk_resource']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['apikey', 'X-Api-Key']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/queue/bulk', 'DELETE',
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
    def get_queue(self, page : Optional[StrictInt] = None, page_size : Optional[StrictInt] = None, sort_key : Optional[StrictStr] = None, sort_direction : Optional[SortDirection] = None, include_unknown_artist_items : Optional[StrictBool] = None, include_artist : Optional[StrictBool] = None, include_album : Optional[StrictBool] = None, artist_ids : Optional[conlist(StrictInt)] = None, protocol : Optional[DownloadProtocol] = None, quality : Optional[StrictInt] = None, **kwargs) -> QueueResourcePagingResource:  # noqa: E501
        """get_queue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_queue(page, page_size, sort_key, sort_direction, include_unknown_artist_items, include_artist, include_album, artist_ids, protocol, quality, async_req=True)
        >>> result = thread.get()

        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param sort_key:
        :type sort_key: str
        :param sort_direction:
        :type sort_direction: SortDirection
        :param include_unknown_artist_items:
        :type include_unknown_artist_items: bool
        :param include_artist:
        :type include_artist: bool
        :param include_album:
        :type include_album: bool
        :param artist_ids:
        :type artist_ids: List[int]
        :param protocol:
        :type protocol: DownloadProtocol
        :param quality:
        :type quality: int
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
        :rtype: QueueResourcePagingResource
        """
        kwargs['_return_http_data_only'] = True
        return self.get_queue_with_http_info(page, page_size, sort_key, sort_direction, include_unknown_artist_items, include_artist, include_album, artist_ids, protocol, quality, **kwargs)  # noqa: E501

    @validate_arguments
    def get_queue_with_http_info(self, page : Optional[StrictInt] = None, page_size : Optional[StrictInt] = None, sort_key : Optional[StrictStr] = None, sort_direction : Optional[SortDirection] = None, include_unknown_artist_items : Optional[StrictBool] = None, include_artist : Optional[StrictBool] = None, include_album : Optional[StrictBool] = None, artist_ids : Optional[conlist(StrictInt)] = None, protocol : Optional[DownloadProtocol] = None, quality : Optional[StrictInt] = None, **kwargs):  # noqa: E501
        """get_queue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_queue_with_http_info(page, page_size, sort_key, sort_direction, include_unknown_artist_items, include_artist, include_album, artist_ids, protocol, quality, async_req=True)
        >>> result = thread.get()

        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param sort_key:
        :type sort_key: str
        :param sort_direction:
        :type sort_direction: SortDirection
        :param include_unknown_artist_items:
        :type include_unknown_artist_items: bool
        :param include_artist:
        :type include_artist: bool
        :param include_album:
        :type include_album: bool
        :param artist_ids:
        :type artist_ids: List[int]
        :param protocol:
        :type protocol: DownloadProtocol
        :param quality:
        :type quality: int
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
        :rtype: tuple(QueueResourcePagingResource, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'page',
            'page_size',
            'sort_key',
            'sort_direction',
            'include_unknown_artist_items',
            'include_artist',
            'include_album',
            'artist_ids',
            'protocol',
            'quality'
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
                    " to method get_queue" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))
        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))
        if _params.get('sort_key') is not None:  # noqa: E501
            _query_params.append(('sortKey', _params['sort_key']))
        if _params.get('sort_direction') is not None:  # noqa: E501
            _query_params.append(('sortDirection', _params['sort_direction']))
        if _params.get('include_unknown_artist_items') is not None:  # noqa: E501
            _query_params.append(('includeUnknownArtistItems', _params['include_unknown_artist_items']))
        if _params.get('include_artist') is not None:  # noqa: E501
            _query_params.append(('includeArtist', _params['include_artist']))
        if _params.get('include_album') is not None:  # noqa: E501
            _query_params.append(('includeAlbum', _params['include_album']))
        if _params.get('artist_ids') is not None:  # noqa: E501
            _query_params.append(('artistIds', _params['artist_ids']))
            _collection_formats['artistIds'] = 'multi'
        if _params.get('protocol') is not None:  # noqa: E501
            _query_params.append(('protocol', _params['protocol']))
        if _params.get('quality') is not None:  # noqa: E501
            _query_params.append(('quality', _params['quality']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apikey', 'X-Api-Key']  # noqa: E501

        _response_types_map = {
            '200': "QueueResourcePagingResource",
        }

        return self.api_client.call_api(
            '/api/v1/queue', 'GET',
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
