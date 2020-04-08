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
from LAMP.api.api_api import APIApi
from LAMP.rest import ApiException


class TestAPIApi(unittest.TestCase):
    """APIApi unit test stubs"""

    def setUp(self):
        self.api = LAMP.api.api_api.APIApi()

    def tearDown(self):
        pass

    def test_query(self):
        """Test case for query

        Query the LAMP Database.
        """
        pass

    def test_schema(self):
        """Test case for schema

        View the API schema document.
        """
        pass


if __name__ == '__main__':
    unittest.main()
