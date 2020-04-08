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
from LAMP.api.type_api import TypeApi
from LAMP.rest import ApiException


class TestTypeApi(unittest.TestCase):
    """TypeApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.type_api.TypeApi()

    def tearDown(self):
        pass

    def test_get_attachment(self):
        """Test case for get_attachment

        """
        pass

    def test_get_dynamic_attachment(self):
        """Test case for get_dynamic_attachment

        """
        pass

    def test_list_attachments(self):
        """Test case for list_attachments

        """
        pass

    def test_parent(self):
        """Test case for parent

        Find the owner(s) of the resource.
        """
        pass

    def test_set_attachment(self):
        """Test case for set_attachment

        """
        pass

    def test_set_dynamic_attachment(self):
        """Test case for set_dynamic_attachment

        """
        pass


if __name__ == '__main__':
    unittest.main()
