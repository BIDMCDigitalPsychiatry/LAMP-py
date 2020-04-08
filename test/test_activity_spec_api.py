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
from LAMP.api.activity_spec_api import ActivitySpecApi
from LAMP.rest import ApiException


class TestActivitySpecApi(unittest.TestCase):
    """ActivitySpecApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.activity_spec_api.ActivitySpecApi()

    def tearDown(self):
        pass

    def test_all(self):
        """Test case for all

        Get all ActivitySpecs registered.
        """
        pass

    def test_create(self):
        """Test case for create

        Create a new ActivitySpec.
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete an ActivitySpec.
        """
        pass

    def test_update(self):
        """Test case for update

        Update an ActivitySpec.
        """
        pass

    def test_view(self):
        """Test case for view

        View an ActivitySpec.
        """
        pass


if __name__ == '__main__':
    unittest.main()
