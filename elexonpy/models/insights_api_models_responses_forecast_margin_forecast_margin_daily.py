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

class InsightsApiModelsResponsesForecastMarginForecastMarginDaily(object):
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
        'publish_time': 'datetime',
        'margin': 'int',
        'forecast_date': 'date'
    }

    attribute_map = {
        'publish_time': 'publishTime',
        'margin': 'margin',
        'forecast_date': 'forecastDate'
    }

    def __init__(self, publish_time=None, margin=None, forecast_date=None):  # noqa: E501
        """InsightsApiModelsResponsesForecastMarginForecastMarginDaily - a model defined in Swagger"""  # noqa: E501
        self._publish_time = None
        self._margin = None
        self._forecast_date = None
        self.discriminator = None
        if publish_time is not None:
            self.publish_time = publish_time
        if margin is not None:
            self.margin = margin
        if forecast_date is not None:
            self.forecast_date = forecast_date

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def margin(self):
        """Gets the margin of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.  # noqa: E501


        :return: The margin of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.  # noqa: E501
        :rtype: int
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.


        :param margin: The margin of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.  # noqa: E501
        :type: int
        """

        self._margin = margin

    @property
    def forecast_date(self):
        """Gets the forecast_date of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.  # noqa: E501


        :return: The forecast_date of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.  # noqa: E501
        :rtype: date
        """
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, forecast_date):
        """Sets the forecast_date of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.


        :param forecast_date: The forecast_date of this InsightsApiModelsResponsesForecastMarginForecastMarginDaily.  # noqa: E501
        :type: date
        """

        self._forecast_date = forecast_date

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
        if issubclass(InsightsApiModelsResponsesForecastMarginForecastMarginDaily, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesForecastMarginForecastMarginDaily):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
