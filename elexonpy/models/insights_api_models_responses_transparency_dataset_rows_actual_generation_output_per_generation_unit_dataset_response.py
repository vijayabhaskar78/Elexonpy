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

class InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse(object):
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
        'psr_type': 'str',
        'bm_unit': 'str',
        'national_grid_bm_unit_id': 'str',
        'settlement_date': 'date',
        'settlement_period': 'int',
        'half_hour_end_time': 'datetime',
        'quantity': 'float'
    }

    attribute_map = {
        'dataset': 'dataset',
        'psr_type': 'psrType',
        'bm_unit': 'bmUnit',
        'national_grid_bm_unit_id': 'nationalGridBmUnitId',
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'half_hour_end_time': 'halfHourEndTime',
        'quantity': 'quantity'
    }

    def __init__(self, dataset=None, psr_type=None, bm_unit=None, national_grid_bm_unit_id=None, settlement_date=None, settlement_period=None, half_hour_end_time=None, quantity=None):  # noqa: E501
        """InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._psr_type = None
        self._bm_unit = None
        self._national_grid_bm_unit_id = None
        self._settlement_date = None
        self._settlement_period = None
        self._half_hour_end_time = None
        self._quantity = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if psr_type is not None:
            self.psr_type = psr_type
        if bm_unit is not None:
            self.bm_unit = bm_unit
        if national_grid_bm_unit_id is not None:
            self.national_grid_bm_unit_id = national_grid_bm_unit_id
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if half_hour_end_time is not None:
            self.half_hour_end_time = half_hour_end_time
        if quantity is not None:
            self.quantity = quantity

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.


        :param dataset: The dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def psr_type(self):
        """Gets the psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501


        :return: The psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._psr_type

    @psr_type.setter
    def psr_type(self, psr_type):
        """Sets the psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.


        :param psr_type: The psr_type of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :type: str
        """

        self._psr_type = psr_type

    @property
    def bm_unit(self):
        """Gets the bm_unit of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501


        :return: The bm_unit of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._bm_unit

    @bm_unit.setter
    def bm_unit(self, bm_unit):
        """Sets the bm_unit of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.


        :param bm_unit: The bm_unit of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :type: str
        """

        self._bm_unit = bm_unit

    @property
    def national_grid_bm_unit_id(self):
        """Gets the national_grid_bm_unit_id of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501


        :return: The national_grid_bm_unit_id of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._national_grid_bm_unit_id

    @national_grid_bm_unit_id.setter
    def national_grid_bm_unit_id(self, national_grid_bm_unit_id):
        """Sets the national_grid_bm_unit_id of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.


        :param national_grid_bm_unit_id: The national_grid_bm_unit_id of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :type: str
        """

        self._national_grid_bm_unit_id = national_grid_bm_unit_id

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def half_hour_end_time(self):
        """Gets the half_hour_end_time of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501


        :return: The half_hour_end_time of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._half_hour_end_time

    @half_hour_end_time.setter
    def half_hour_end_time(self, half_hour_end_time):
        """Sets the half_hour_end_time of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.


        :param half_hour_end_time: The half_hour_end_time of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :type: datetime
        """

        self._half_hour_end_time = half_hour_end_time

    @property
    def quantity(self):
        """Gets the quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501


        :return: The quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.


        :param quantity: The quantity of this InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

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
        if issubclass(InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
