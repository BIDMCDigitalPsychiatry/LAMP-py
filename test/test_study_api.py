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
from LAMP.api.study_api import StudyApi
from LAMP.rest import ApiException


class TestStudyApi(unittest.TestCase):
    """StudyApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.study_api.StudyApi()

    def tearDown(self):
        pass

    def test_all(self):
        """Test case for all

        Get the set of all studies.
        """
        pass

    def test_all_by_researcher(self):
        """Test case for all_by_researcher

        Get the set of studies for a single researcher.
        """
        pass

    def test_create(self):
        """Test case for create

        Create a new Study for the given Researcher.
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a study.
        """
        pass

    def test_update(self):
        """Test case for update

        Update the study.
        """
        pass

    def test_view(self):
        """Test case for view

        Get a single study, by identifier.
        """
        pass


if __name__ == '__main__':
    unittest.main()
