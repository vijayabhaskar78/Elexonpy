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

class InsightsApiLegacyInteroperabilityLegacyRemitDetailBody(object):
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
        'data_item': 'str',
        'list': 'InsightsApiLegacyInteroperabilityLegacyRemitDetailList'
    }

    attribute_map = {
        'data_item': 'dataItem',
        'list': 'list'
    }

    def __init__(self, data_item=None, list=None):  # noqa: E501
        """InsightsApiLegacyInteroperabilityLegacyRemitDetailBody - a model defined in Swagger"""  # noqa: E501
        self._data_item = None
        self._list = None
        self.discriminator = None
        if data_item is not None:
            self.data_item = data_item
        if list is not None:
            self.list = list

    @property
    def data_item(self):
        """Gets the data_item of this InsightsApiLegacyInteroperabilityLegacyRemitDetailBody.  # noqa: E501


        :return: The data_item of this InsightsApiLegacyInteroperabilityLegacyRemitDetailBody.  # noqa: E501
        :rtype: str
        """
        return self._data_item

    @data_item.setter
    def data_item(self, data_item):
        """Sets the data_item of this InsightsApiLegacyInteroperabilityLegacyRemitDetailBody.


        :param data_item: The data_item of this InsightsApiLegacyInteroperabilityLegacyRemitDetailBody.  # noqa: E501
        :type: str
        """

        self._data_item = data_item

    @property
    def list(self):
        """Gets the list of this InsightsApiLegacyInteroperabilityLegacyRemitDetailBody.  # noqa: E501


        :return: The list of this InsightsApiLegacyInteroperabilityLegacyRemitDetailBody.  # noqa: E501
        :rtype: InsightsApiLegacyInteroperabilityLegacyRemitDetailList
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this InsightsApiLegacyInteroperabilityLegacyRemitDetailBody.


        :param list: The list of this InsightsApiLegacyInteroperabilityLegacyRemitDetailBody.  # noqa: E501
        :type: InsightsApiLegacyInteroperabilityLegacyRemitDetailList
        """

        self._list = list

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
        if issubclass(InsightsApiLegacyInteroperabilityLegacyRemitDetailBody, dict):
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
        if not isinstance(other, InsightsApiLegacyInteroperabilityLegacyRemitDetailBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
