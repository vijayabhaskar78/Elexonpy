# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""



import unittest

import elexonpy
from elexonpy.api.health_check_api import HealthCheckApi  # noqa: E501
from elexonpy.rest import ApiException


class TestHealthCheckApi(unittest.TestCase):
    """HealthCheckApi unit test stubs"""

    def setUp(self):
        self.api = HealthCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_get(self):
        """Test case for health_get

        Health check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
