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
from LAMP.api.sensor_event_api import SensorEventApi
from LAMP.rest import ApiException


class TestSensorEventApi(unittest.TestCase):
    """SensorEventApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.sensor_event_api.SensorEventApi()

    def tearDown(self):
        pass

    def test_all_by_participant(self):
        """Test case for all_by_participant

        Get all sensor events for a participant.
        """
        pass

    def test_all_by_researcher(self):
        """Test case for all_by_researcher

        Get all sensor events for a researcher by participant.
        """
        pass

    def test_all_by_study(self):
        """Test case for all_by_study

        Get all sensor events for a study by participant.
        """
        pass

    def test_create(self):
        """Test case for create

        Create a new SensorEvent for the given Participant.
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a sensor event.
        """
        pass


if __name__ == '__main__':
    unittest.main()
