# coding: utf-8

"""
    Insights API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""



import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from elexonpy.api_client import ApiClient


class BidOfferApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s(self, settlement_date, settlement_period, **kwargs):  # noqa: E501
        """Market-wide bid-offer data (BOD)  # noqa: E501

        This endpoint provides market-wide bid-offer data, for all BMUs or a requested set of multiple BMUs.  It returns the data valid for a given settlement period, excluding any results where LevelFrom and LevelTo are both zero.                The settlement period to query must be specified as a date and settlement period. The date should be provided in the format yyyy-MM-dd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s(settlement_date, settlement_period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date settlement_date: Format - date (as full-date in RFC3339). The settlement date to filter. (required)
        :param int settlement_period: Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive. (required)
        :param list[str] bm_unit: The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned.
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s_with_http_info(settlement_date, settlement_period, **kwargs)  # noqa: E501
        else:
            (data) = self.get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s_with_http_info(settlement_date, settlement_period, **kwargs)  # noqa: E501
            return data

    def get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s_with_http_info(self, settlement_date, settlement_period, **kwargs):  # noqa: E501
        """Market-wide bid-offer data (BOD)  # noqa: E501

        This endpoint provides market-wide bid-offer data, for all BMUs or a requested set of multiple BMUs.  It returns the data valid for a given settlement period, excluding any results where LevelFrom and LevelTo are both zero.                The settlement period to query must be specified as a date and settlement period. The date should be provided in the format yyyy-MM-dd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s_with_http_info(settlement_date, settlement_period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date settlement_date: Format - date (as full-date in RFC3339). The settlement date to filter. (required)
        :param int settlement_period: Format - int32. The settlement period to filter. This should be an integer from 1-50 inclusive. (required)
        :param list[str] bm_unit: The BM Units to query. Elexon or NGC BMU IDs can be used. If omitted, results for all BM units will be returned.
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settlement_date', 'settlement_period', 'bm_unit', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settlement_date' is set
        if ('settlement_date' not in params or
                params['settlement_date'] is None):
            raise ValueError("Missing the required parameter `settlement_date` when calling `get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s`")  # noqa: E501
        # verify the required parameter 'settlement_period' is set
        if ('settlement_period' not in params or
                params['settlement_period'] is None):
            raise ValueError("Missing the required parameter `settlement_period` when calling `get_balancing_bid_offer_all_settlementdate_settlementdate_settlementperiod_s`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'settlement_date' in params:
            query_params.append(('settlementDate', params['settlement_date']))  # noqa: E501
        if 'settlement_period' in params:
            query_params.append(('settlementPeriod', params['settlement_period']))  # noqa: E501
        if 'bm_unit' in params:
            query_params.append(('bmUnit', params['bm_unit']))  # noqa: E501
            collection_formats['bmUnit'] = 'multi'  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/balancing/bid-offer/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_balancing_bid_offer_bmunit_bmunit_from_from_to_to(self, bm_unit, _from, to, **kwargs):  # noqa: E501
        """Bid-offer data per BMU (BOD)  # noqa: E501

        This endpoint provides the bid-offer data for a requested BMU. It returns the data valid over a given time  range, excluding any results where LevelFrom and LevelTo are both zero.                By default, the from and to parameters filter the data inclusively and this endpoint will return any data that  overlaps even at a single instant. If the settlementPeriodFrom or settlementPeriodTo parameters are provided, it  will instead filter to return any data that overlaps with the specified range of settlement periods. It is  possible to search using a combination of time and/or settlement date & settlement period. Note: When  filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For example,  2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering by timeFrom and timeTo:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from timeFrom to settlement date and period:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to TimeTo:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_balancing_bid_offer_bmunit_bmunit_from_from_to_to(bm_unit, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bm_unit: The BM Unit to query. (required)
        :param datetime _from: Format - date-time (as date-time in RFC3339). The \"from\" start time or settlement date for the filter. (required)
        :param datetime to: Format - date-time (as date-time in RFC3339). The \"to\" start time or settlement date for the filter. (required)
        :param int settlement_period_from: Format - int32. The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :param int settlement_period_to: Format - int32. The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_balancing_bid_offer_bmunit_bmunit_from_from_to_to_with_http_info(bm_unit, _from, to, **kwargs)  # noqa: E501
        else:
            (data) = self.get_balancing_bid_offer_bmunit_bmunit_from_from_to_to_with_http_info(bm_unit, _from, to, **kwargs)  # noqa: E501
            return data

    def get_balancing_bid_offer_bmunit_bmunit_from_from_to_to_with_http_info(self, bm_unit, _from, to, **kwargs):  # noqa: E501
        """Bid-offer data per BMU (BOD)  # noqa: E501

        This endpoint provides the bid-offer data for a requested BMU. It returns the data valid over a given time  range, excluding any results where LevelFrom and LevelTo are both zero.                By default, the from and to parameters filter the data inclusively and this endpoint will return any data that  overlaps even at a single instant. If the settlementPeriodFrom or settlementPeriodTo parameters are provided, it  will instead filter to return any data that overlaps with the specified range of settlement periods. It is  possible to search using a combination of time and/or settlement date & settlement period. Note: When  filtering via settlement date, from/to are treated as Dates only, with the time being ignored. For example,  2022-06-01T00:00Z and 2022-06-01T11:11Z are both treated as the settlement date 2022-06-01.                All Dates and DateTimes should be expressed as defined within  <a href=\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\" target=\"_blank\">RFC 3339</a>.                Some examples of date parameter combinations are shown below.                Filtering by timeFrom and timeTo:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z                Filtering from timeFrom to settlement date and period:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodTo=1                Filtering from settlement date and period to TimeTo:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1                Filtering from settlement date and period to settlement date and period:                    /balancing/bid-offer?bmUnit=T_DRAXX-1&from=2022-06-01T00:00Z&to=2022-07-01T00:00Z&settlementPeriodFrom=1&settlementPeriodTo=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_balancing_bid_offer_bmunit_bmunit_from_from_to_to_with_http_info(bm_unit, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bm_unit: The BM Unit to query. (required)
        :param datetime _from: Format - date-time (as date-time in RFC3339). The \"from\" start time or settlement date for the filter. (required)
        :param datetime to: Format - date-time (as date-time in RFC3339). The \"to\" start time or settlement date for the filter. (required)
        :param int settlement_period_from: Format - int32. The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :param int settlement_period_to: Format - int32. The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive.
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bm_unit', '_from', 'to', 'settlement_period_from', 'settlement_period_to', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_balancing_bid_offer_bmunit_bmunit_from_from_to_to" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bm_unit' is set
        if ('bm_unit' not in params or
                params['bm_unit'] is None):
            raise ValueError("Missing the required parameter `bm_unit` when calling `get_balancing_bid_offer_bmunit_bmunit_from_from_to_to`")  # noqa: E501
        # verify the required parameter '_from' is set
        if ('_from' not in params or
                params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `get_balancing_bid_offer_bmunit_bmunit_from_from_to_to`")  # noqa: E501
        # verify the required parameter 'to' is set
        if ('to' not in params or
                params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `get_balancing_bid_offer_bmunit_bmunit_from_from_to_to`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bm_unit' in params:
            query_params.append(('bmUnit', params['bm_unit']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'settlement_period_from' in params:
            query_params.append(('settlementPeriodFrom', params['settlement_period_from']))  # noqa: E501
        if 'settlement_period_to' in params:
            query_params.append(('settlementPeriodTo', params['settlement_period_to']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/balancing/bid-offer', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
