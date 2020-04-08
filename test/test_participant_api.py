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
from LAMP.api.participant_api import ParticipantApi
from LAMP.rest import ApiException


class TestParticipantApi(unittest.TestCase):
    """ParticipantApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.participant_api.ParticipantApi()

    def tearDown(self):
        pass

    def test_all(self):
        """Test case for all

        Get the set of all participants.
        """
        pass

    def test_all_by_researcher(self):
        """Test case for all_by_researcher

        Get the set of all participants under a single researcher.
        """
        pass

    def test_all_by_study(self):
        """Test case for all_by_study

        Get the set of all participants in a single study.
        """
        pass

    def test_create(self):
        """Test case for create

        Create a new Participant for the given Study.
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a participant AND all owned data or event streams.
        """
        pass

    def test_update(self):
        """Test case for update

        Update a Participant's settings.
        """
        pass

    def test_view(self):
        """Test case for view

        Get a single participant, by identifier.
        """
        pass


if __name__ == '__main__':
    unittest.main()
