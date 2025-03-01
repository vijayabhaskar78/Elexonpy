# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dataset': 'str',
        'settlement_date': 'date',
        'settlement_period': 'int',
        'time_from': 'datetime',
        'level_from': 'int',
        'time_to': 'datetime',
        'level_to': 'int',
        'pair_id': 'int',
        'offer': 'float',
        'bid': 'float',
        'national_grid_bm_unit': 'str',
        'bm_unit': 'str'
    }

    attribute_map = {
        'dataset': 'dataset',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'time_from': 'timeFrom',
        'level_from': 'levelFrom',
        'time_to': 'timeTo',
        'level_to': 'levelTo',
        'pair_id': 'pairId',
        'offer': 'offer',
        'bid': 'bid',
        'national_grid_bm_unit': 'nationalGridBmUnit',
        'bm_unit': 'bmUnit'
    }

    def __init__(self, dataset=None, settlement_date=None, settlement_period=None, time_from=None, level_from=None, time_to=None, level_to=None, pair_id=None, offer=None, bid=None, national_grid_bm_unit=None, bm_unit=None):  # noqa: E501
        """InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._settlement_date = None
        self._settlement_period = None
        self._time_from = None
        self._level_from = None
        self._time_to = None
        self._level_to = None
        self._pair_id = None
        self._offer = None
        self._bid = None
        self._national_grid_bm_unit = None
        self._bm_unit = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if time_from is not None:
            self.time_from = time_from
        if level_from is not None:
            self.level_from = level_from
        if time_to is not None:
            self.time_to = time_to
        if level_to is not None:
            self.level_to = level_to
        if pair_id is not None:
            self.pair_id = pair_id
        if offer is not None:
            self.offer = offer
        if bid is not None:
            self.bid = bid
        if national_grid_bm_unit is not None:
            self.national_grid_bm_unit = national_grid_bm_unit
        if bm_unit is not None:
            self.bm_unit = bm_unit

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param dataset: The dataset of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def time_from(self):
        """Gets the time_from of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The time_from of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_from

    @time_from.setter
    def time_from(self, time_from):
        """Sets the time_from of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param time_from: The time_from of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: datetime
        """

        self._time_from = time_from

    @property
    def level_from(self):
        """Gets the level_from of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The level_from of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: int
        """
        return self._level_from

    @level_from.setter
    def level_from(self, level_from):
        """Sets the level_from of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param level_from: The level_from of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: int
        """

        self._level_from = level_from

    @property
    def time_to(self):
        """Gets the time_to of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The time_to of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_to

    @time_to.setter
    def time_to(self, time_to):
        """Sets the time_to of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param time_to: The time_to of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: datetime
        """

        self._time_to = time_to

    @property
    def level_to(self):
        """Gets the level_to of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The level_to of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: int
        """
        return self._level_to

    @level_to.setter
    def level_to(self, level_to):
        """Sets the level_to of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param level_to: The level_to of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: int
        """

        self._level_to = level_to

    @property
    def pair_id(self):
        """Gets the pair_id of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The pair_id of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: int
        """
        return self._pair_id

    @pair_id.setter
    def pair_id(self, pair_id):
        """Sets the pair_id of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param pair_id: The pair_id of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: int
        """

        self._pair_id = pair_id

    @property
    def offer(self):
        """Gets the offer of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The offer of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: float
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param offer: The offer of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: float
        """

        self._offer = offer

    @property
    def bid(self):
        """Gets the bid of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The bid of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: float
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param bid: The bid of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: float
        """

        self._bid = bid

    @property
    def national_grid_bm_unit(self):
        """Gets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._national_grid_bm_unit

    @national_grid_bm_unit.setter
    def national_grid_bm_unit(self, national_grid_bm_unit):
        """Sets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param national_grid_bm_unit: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: str
        """

        self._national_grid_bm_unit = national_grid_bm_unit

    @property
    def bm_unit(self):
        """Gets the bm_unit of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501


        :return: The bm_unit of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._bm_unit

    @bm_unit.setter
    def bm_unit(self, bm_unit):
        """Sets the bm_unit of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.


        :param bm_unit: The bm_unit of this InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.  # noqa: E501
        :type: str
        """

        self._bm_unit = bm_unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
            else:
                result[attr] = value
        if issubclass(InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse, dict):
            for key, value in list(self.items()):
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
