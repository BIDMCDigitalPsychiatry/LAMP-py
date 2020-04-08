# coding: utf-8

"""
    LAMP Platform

    The LAMP Platform API.

    The version of the OpenAPI document: 1.0.0
    Contact: team@digitalpsych.org
"""


from __future__ import absolute_import
import re
import sys

import six
import nulltype

from LAMP.model_utils import (
    ModelComposed,
    ModelNormal,
    ModelSimple,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)


class ActivitySpec(ModelNormal):
    """Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    @staticmethod
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'name': (str,),
            'help_contents': (str,),
            'script_contents': (str,),
            'static_data_schema': (bool, date, datetime, dict, float, int, list, str,),
            'temporal_event_schema': (bool, date, datetime, dict, float, int, list, str,),
            'settings_schema': (bool, date, datetime, dict, float, int, list, str,),
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'name': 'name',
        'help_contents': 'help_contents',
        'script_contents': 'script_contents',
        'static_data_schema': 'static_data_schema',
        'temporal_event_schema': 'temporal_event_schema',
        'settings_schema': 'settings_schema',
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
    ])

    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs):
        """activity_spec.ActivitySpec - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            name (str): The name of the activity spec.. [optional]
            help_contents (str): Either a binary blob containing a document or video, or a string containing  instructional aid about the Activity.. [optional]
            script_contents (str): The WebView-compatible script that provides this Activity on mobile or desktop (IFrame) clients.. [optional]
            static_data_schema (bool, date, datetime, dict, float, int, list, str): The static data definition of an ActivitySpec.. [optional]
            temporal_event_schema (bool, date, datetime, dict, float, int, list, str): The temporal event data definition of an ActivitySpec.. [optional]
            settings_schema (bool, date, datetime, dict, float, int, list, str): The Activity settings definition of an ActivitySpec.. [optional]
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
