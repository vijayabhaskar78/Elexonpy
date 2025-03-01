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

class InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData(object):
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
        'publish_time': 'datetime',
        'publishing_period_commencing_time': 'datetime',
        'start_time': 'datetime',
        'settlement_date': 'date',
        'settlement_period': 'int',
        'loss_of_load_probability': 'float',
        'derated_margin': 'float'
    }

    attribute_map = {
        'dataset': 'dataset',
        'publish_time': 'publishTime',
        'publishing_period_commencing_time': 'publishingPeriodCommencingTime',
        'start_time': 'startTime',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'loss_of_load_probability': 'lossOfLoadProbability',
        'derated_margin': 'deratedMargin'
    }

    def __init__(self, dataset=None, publish_time=None, publishing_period_commencing_time=None, start_time=None, settlement_date=None, settlement_period=None, loss_of_load_probability=None, derated_margin=None):  # noqa: E501
        """InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._publish_time = None
        self._publishing_period_commencing_time = None
        self._start_time = None
        self._settlement_date = None
        self._settlement_period = None
        self._loss_of_load_probability = None
        self._derated_margin = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if publish_time is not None:
            self.publish_time = publish_time
        if publishing_period_commencing_time is not None:
            self.publishing_period_commencing_time = publishing_period_commencing_time
        if start_time is not None:
            self.start_time = start_time
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if loss_of_load_probability is not None:
            self.loss_of_load_probability = loss_of_load_probability
        if derated_margin is not None:
            self.derated_margin = derated_margin

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.


        :param dataset: The dataset of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def publishing_period_commencing_time(self):
        """Gets the publishing_period_commencing_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501


        :return: The publishing_period_commencing_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :rtype: datetime
        """
        return self._publishing_period_commencing_time

    @publishing_period_commencing_time.setter
    def publishing_period_commencing_time(self, publishing_period_commencing_time):
        """Sets the publishing_period_commencing_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.


        :param publishing_period_commencing_time: The publishing_period_commencing_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :type: datetime
        """

        self._publishing_period_commencing_time = publishing_period_commencing_time

    @property
    def start_time(self):
        """Gets the start_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501


        :return: The start_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.


        :param start_time: The start_time of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def loss_of_load_probability(self):
        """Gets the loss_of_load_probability of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501


        :return: The loss_of_load_probability of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :rtype: float
        """
        return self._loss_of_load_probability

    @loss_of_load_probability.setter
    def loss_of_load_probability(self, loss_of_load_probability):
        """Sets the loss_of_load_probability of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.


        :param loss_of_load_probability: The loss_of_load_probability of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :type: float
        """

        self._loss_of_load_probability = loss_of_load_probability

    @property
    def derated_margin(self):
        """Gets the derated_margin of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501


        :return: The derated_margin of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :rtype: float
        """
        return self._derated_margin

    @derated_margin.setter
    def derated_margin(self, derated_margin):
        """Sets the derated_margin of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.


        :param derated_margin: The derated_margin of this InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.  # noqa: E501
        :type: float
        """

        self._derated_margin = derated_margin

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
        if issubclass(InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
