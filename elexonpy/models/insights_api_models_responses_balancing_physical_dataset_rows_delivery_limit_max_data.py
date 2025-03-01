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

class InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData(object):
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
        'time_to': 'datetime',
        'level_from': 'int',
        'level_to': 'int',
        'notification_time': 'datetime',
        'notification_sequence': 'int',
        'national_grid_bm_unit': 'str',
        'bm_unit': 'str'
    }

    attribute_map = {
        'dataset': 'dataset',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'time_from': 'timeFrom',
        'time_to': 'timeTo',
        'level_from': 'levelFrom',
        'level_to': 'levelTo',
        'notification_time': 'notificationTime',
        'notification_sequence': 'notificationSequence',
        'national_grid_bm_unit': 'nationalGridBmUnit',
        'bm_unit': 'bmUnit'
    }

    def __init__(self, dataset=None, settlement_date=None, settlement_period=None, time_from=None, time_to=None, level_from=None, level_to=None, notification_time=None, notification_sequence=None, national_grid_bm_unit=None, bm_unit=None):  # noqa: E501
        """InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._settlement_date = None
        self._settlement_period = None
        self._time_from = None
        self._time_to = None
        self._level_from = None
        self._level_to = None
        self._notification_time = None
        self._notification_sequence = None
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
        if time_to is not None:
            self.time_to = time_to
        if level_from is not None:
            self.level_from = level_from
        if level_to is not None:
            self.level_to = level_to
        if notification_time is not None:
            self.notification_time = notification_time
        if notification_sequence is not None:
            self.notification_sequence = notification_sequence
        if national_grid_bm_unit is not None:
            self.national_grid_bm_unit = national_grid_bm_unit
        if bm_unit is not None:
            self.bm_unit = bm_unit

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param dataset: The dataset of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def time_from(self):
        """Gets the time_from of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The time_from of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: datetime
        """
        return self._time_from

    @time_from.setter
    def time_from(self, time_from):
        """Sets the time_from of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param time_from: The time_from of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: datetime
        """

        self._time_from = time_from

    @property
    def time_to(self):
        """Gets the time_to of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The time_to of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: datetime
        """
        return self._time_to

    @time_to.setter
    def time_to(self, time_to):
        """Sets the time_to of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param time_to: The time_to of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: datetime
        """

        self._time_to = time_to

    @property
    def level_from(self):
        """Gets the level_from of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The level_from of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: int
        """
        return self._level_from

    @level_from.setter
    def level_from(self, level_from):
        """Sets the level_from of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param level_from: The level_from of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: int
        """

        self._level_from = level_from

    @property
    def level_to(self):
        """Gets the level_to of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The level_to of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: int
        """
        return self._level_to

    @level_to.setter
    def level_to(self, level_to):
        """Sets the level_to of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param level_to: The level_to of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: int
        """

        self._level_to = level_to

    @property
    def notification_time(self):
        """Gets the notification_time of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The notification_time of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: datetime
        """
        return self._notification_time

    @notification_time.setter
    def notification_time(self, notification_time):
        """Sets the notification_time of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param notification_time: The notification_time of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: datetime
        """

        self._notification_time = notification_time

    @property
    def notification_sequence(self):
        """Gets the notification_sequence of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The notification_sequence of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: int
        """
        return self._notification_sequence

    @notification_sequence.setter
    def notification_sequence(self, notification_sequence):
        """Sets the notification_sequence of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param notification_sequence: The notification_sequence of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: int
        """

        self._notification_sequence = notification_sequence

    @property
    def national_grid_bm_unit(self):
        """Gets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: str
        """
        return self._national_grid_bm_unit

    @national_grid_bm_unit.setter
    def national_grid_bm_unit(self, national_grid_bm_unit):
        """Sets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param national_grid_bm_unit: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :type: str
        """

        self._national_grid_bm_unit = national_grid_bm_unit

    @property
    def bm_unit(self):
        """Gets the bm_unit of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501


        :return: The bm_unit of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
        :rtype: str
        """
        return self._bm_unit

    @bm_unit.setter
    def bm_unit(self, bm_unit):
        """Sets the bm_unit of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.


        :param bm_unit: The bm_unit of this InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.  # noqa: E501
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
        if issubclass(InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
