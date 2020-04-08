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
from LAMP.api.sensor_api import SensorApi
from LAMP.rest import ApiException


class TestSensorApi(unittest.TestCase):
    """SensorApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.sensor_api.SensorApi()

    def tearDown(self):
        pass

    def test_all(self):
        """Test case for all

        Get the set of all sensors.
        """
        pass

    def test_all_by_participant(self):
        """Test case for all_by_participant

        Get all sensors for a participant.
        """
        pass

    def test_all_by_researcher(self):
        """Test case for all_by_researcher

        Get all sensors for a researcher.
        """
        pass

    def test_all_by_study(self):
        """Test case for all_by_study

        View all sensors in a study.
        """
        pass

    def test_create(self):
        """Test case for create

        Create a new Sensor under the given Study.
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a Sensor.
        """
        pass

    def test_update(self):
        """Test case for update

        Update an Sensor's settings.
        """
        pass

    def test_view(self):
        """Test case for view

        Get a single sensor, by identifier.
        """
        pass


if __name__ == '__main__':
    unittest.main()
