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
from LAMP.api.researcher_api import ResearcherApi
from LAMP.rest import ApiException


class TestResearcherApi(unittest.TestCase):
    """ResearcherApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.researcher_api.ResearcherApi()

    def tearDown(self):
        pass

    def test_all(self):
        """Test case for all

        Get the set of all researchers.
        """
        pass

    def test_create(self):
        """Test case for create

        Create a new Researcher.
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a researcher.
        """
        pass

    def test_update(self):
        """Test case for update

        Update a Researcher's settings.
        """
        pass

    def test_view(self):
        """Test case for view

        Get a single researcher, by identifier.
        """
        pass


if __name__ == '__main__':
    unittest.main()
