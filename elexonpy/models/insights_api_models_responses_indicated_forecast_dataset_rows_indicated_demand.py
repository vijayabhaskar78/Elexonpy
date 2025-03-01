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

class InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand(object):
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
        'demand': 'int',
        'publish_time': 'datetime',
        'start_time': 'datetime',
        'settlement_date': 'date',
        'settlement_period': 'int',
        'boundary': 'str'
    }

    attribute_map = {
        'dataset': 'dataset',
        'demand': 'demand',
        'publish_time': 'publishTime',
        'start_time': 'startTime',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'boundary': 'boundary'
    }

    def __init__(self, dataset=None, demand=None, publish_time=None, start_time=None, settlement_date=None, settlement_period=None, boundary=None):  # noqa: E501
        """InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._demand = None
        self._publish_time = None
        self._start_time = None
        self._settlement_date = None
        self._settlement_period = None
        self._boundary = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if demand is not None:
            self.demand = demand
        if publish_time is not None:
            self.publish_time = publish_time
        if start_time is not None:
            self.start_time = start_time
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if boundary is not None:
            self.boundary = boundary

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.


        :param dataset: The dataset of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def demand(self):
        """Gets the demand of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501


        :return: The demand of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :rtype: int
        """
        return self._demand

    @demand.setter
    def demand(self, demand):
        """Sets the demand of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.


        :param demand: The demand of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :type: int
        """

        self._demand = demand

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def start_time(self):
        """Gets the start_time of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501


        :return: The start_time of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.


        :param start_time: The start_time of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def boundary(self):
        """Gets the boundary of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501


        :return: The boundary of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :rtype: str
        """
        return self._boundary

    @boundary.setter
    def boundary(self, boundary):
        """Sets the boundary of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.


        :param boundary: The boundary of this InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.  # noqa: E501
        :type: str
        """

        self._boundary = boundary

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
        if issubclass(InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
