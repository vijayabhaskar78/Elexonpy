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

class InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse(object):
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
        'metadata': 'InsightsApiLegacyInteroperabilityLegacyRemitDetailMetadata',
        'body': 'InsightsApiLegacyInteroperabilityLegacyRemitDetailBody'
    }

    attribute_map = {
        'metadata': 'metadata',
        'body': 'body'
    }

    def __init__(self, metadata=None, body=None):  # noqa: E501
        """InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse - a model defined in Swagger"""  # noqa: E501
        self._metadata = None
        self._body = None
        self.discriminator = None
        if metadata is not None:
            self.metadata = metadata
        if body is not None:
            self.body = body

    @property
    def metadata(self):
        """Gets the metadata of this InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.  # noqa: E501


        :return: The metadata of this InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.  # noqa: E501
        :rtype: InsightsApiLegacyInteroperabilityLegacyRemitDetailMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.


        :param metadata: The metadata of this InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.  # noqa: E501
        :type: InsightsApiLegacyInteroperabilityLegacyRemitDetailMetadata
        """

        self._metadata = metadata

    @property
    def body(self):
        """Gets the body of this InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.  # noqa: E501


        :return: The body of this InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.  # noqa: E501
        :rtype: InsightsApiLegacyInteroperabilityLegacyRemitDetailBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.


        :param body: The body of this InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.  # noqa: E501
        :type: InsightsApiLegacyInteroperabilityLegacyRemitDetailBody
        """

        self._body = body

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
        if issubclass(InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse, dict):
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
        if not isinstance(other, InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
