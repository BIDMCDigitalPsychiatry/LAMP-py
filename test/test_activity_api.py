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
from LAMP.api.activity_api import ActivityApi
from LAMP.rest import ApiException


class TestActivityApi(unittest.TestCase):
    """ActivityApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.activity_api.ActivityApi()

    def tearDown(self):
        pass

    def test_all(self):
        """Test case for all

        Get the set of all activities.
        """
        pass

    def test_all_by_participant(self):
        """Test case for all_by_participant

        Get all activities for a participant.
        """
        pass

    def test_all_by_researcher(self):
        """Test case for all_by_researcher

        Get all activities for a researcher.
        """
        pass

    def test_all_by_study(self):
        """Test case for all_by_study

        Get all activities in a study.
        """
        pass

    def test_create(self):
        """Test case for create

        Create a new Activity under the given Study.
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete an Activity.
        """
        pass

    def test_update(self):
        """Test case for update

        Update an Activity's settings.
        """
        pass

    def test_view(self):
        """Test case for view

        Get a single activity, by identifier.
        """
        pass


if __name__ == '__main__':
    unittest.main()
