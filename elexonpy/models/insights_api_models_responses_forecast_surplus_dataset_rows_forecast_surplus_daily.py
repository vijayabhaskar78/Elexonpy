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

class InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily(object):
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
        'forecast_date': 'date',
        'surplus': 'int'
    }

    attribute_map = {
        'dataset': 'dataset',
        'publish_time': 'publishTime',
        'forecast_date': 'forecastDate',
        'surplus': 'surplus'
    }

    def __init__(self, dataset=None, publish_time=None, forecast_date=None, surplus=None):  # noqa: E501
        """InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._publish_time = None
        self._forecast_date = None
        self._surplus = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if publish_time is not None:
            self.publish_time = publish_time
        if forecast_date is not None:
            self.forecast_date = forecast_date
        if surplus is not None:
            self.surplus = surplus

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.


        :param dataset: The dataset of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def forecast_date(self):
        """Gets the forecast_date of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501


        :return: The forecast_date of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501
        :rtype: date
        """
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, forecast_date):
        """Sets the forecast_date of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.


        :param forecast_date: The forecast_date of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501
        :type: date
        """

        self._forecast_date = forecast_date

    @property
    def surplus(self):
        """Gets the surplus of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501


        :return: The surplus of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501
        :rtype: int
        """
        return self._surplus

    @surplus.setter
    def surplus(self, surplus):
        """Sets the surplus of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.


        :param surplus: The surplus of this InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.  # noqa: E501
        :type: int
        """

        self._surplus = surplus

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
        if issubclass(InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
