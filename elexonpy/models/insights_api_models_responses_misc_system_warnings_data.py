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

class InsightsApiModelsResponsesMiscSystemWarningsData(object):
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
        'warning_type': 'str',
        'warning_text': 'str'
    }

    attribute_map = {
        'publish_time': 'publishTime',
        'warning_type': 'warningType',
        'warning_text': 'warningText'
    }

    def __init__(self, publish_time=None, warning_type=None, warning_text=None):  # noqa: E501
        """InsightsApiModelsResponsesMiscSystemWarningsData - a model defined in Swagger"""  # noqa: E501
        self._publish_time = None
        self._warning_type = None
        self._warning_text = None
        self.discriminator = None
        if publish_time is not None:
            self.publish_time = publish_time
        if warning_type is not None:
            self.warning_type = warning_type
        if warning_text is not None:
            self.warning_text = warning_text

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesMiscSystemWarningsData.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesMiscSystemWarningsData.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesMiscSystemWarningsData.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesMiscSystemWarningsData.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def warning_type(self):
        """Gets the warning_type of this InsightsApiModelsResponsesMiscSystemWarningsData.  # noqa: E501


        :return: The warning_type of this InsightsApiModelsResponsesMiscSystemWarningsData.  # noqa: E501
        :rtype: str
        """
        return self._warning_type

    @warning_type.setter
    def warning_type(self, warning_type):
        """Sets the warning_type of this InsightsApiModelsResponsesMiscSystemWarningsData.


        :param warning_type: The warning_type of this InsightsApiModelsResponsesMiscSystemWarningsData.  # noqa: E501
        :type: str
        """

        self._warning_type = warning_type

    @property
    def warning_text(self):
        """Gets the warning_text of this InsightsApiModelsResponsesMiscSystemWarningsData.  # noqa: E501


        :return: The warning_text of this InsightsApiModelsResponsesMiscSystemWarningsData.  # noqa: E501
        :rtype: str
        """
        return self._warning_text

    @warning_text.setter
    def warning_text(self, warning_text):
        """Sets the warning_text of this InsightsApiModelsResponsesMiscSystemWarningsData.


        :param warning_text: The warning_text of this InsightsApiModelsResponsesMiscSystemWarningsData.  # noqa: E501
        :type: str
        """

        self._warning_text = warning_text

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
        if issubclass(InsightsApiModelsResponsesMiscSystemWarningsData, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesMiscSystemWarningsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
