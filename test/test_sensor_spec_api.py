# coding: utf-8

"""
    LAMP Platform

    The LAMP Platform API.

    The version of the OpenAPI document: 1.0.0
    Contact: team@digitalpsych.org
"""


from __future__ import absolute_import

import unittest

import LAMP
from LAMP.api.sensor_spec_api import SensorSpecApi
from LAMP.rest import ApiException


class TestSensorSpecApi(unittest.TestCase):
    """SensorSpecApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.sensor_spec_api.SensorSpecApi()

    def tearDown(self):
        pass

    def test_all(self):
        """Test case for all

        Get all SensorSpecs registered.
        """
        pass

    def test_create(self):
        """Test case for create

        Create a new SensorSpec.
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete an SensorSpec.
        """
        pass

    def test_update(self):
        """Test case for update

        Update an SensorSpec.
        """
        pass

    def test_view(self):
        """Test case for view

        Get a SensorSpec.
        """
        pass


if __name__ == '__main__':
    unittest.main()
