# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 4.7.2
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gate_api.api_client import ApiClient


class WalletApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def transfer(self, transfer, **kwargs):  # noqa: E501
        """Transfer between accounts  # noqa: E501

        Transfer between different accounts. Currently support transfers between the following:  1. spot - margin  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer(transfer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Transfer transfer: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transfer_with_http_info(transfer, **kwargs)  # noqa: E501
        else:
            (data) = self.transfer_with_http_info(transfer, **kwargs)  # noqa: E501
            return data

    def transfer_with_http_info(self, transfer, **kwargs):  # noqa: E501
        """Transfer between accounts  # noqa: E501

        Transfer between different accounts. Currently support transfers between the following:  1. spot - margin  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer_with_http_info(transfer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Transfer transfer: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['transfer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfer" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transfer' is set
        if ('transfer' not in local_var_params or
                local_var_params['transfer'] is None):
            raise ValueError("Missing the required parameter `transfer` when calling `transfer`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transfer' in local_var_params:
            body_params = local_var_params['transfer']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'api_sign', 'api_timestamp']  # noqa: E501

        return self.api_client.call_api(
            '/wallet/transfers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
