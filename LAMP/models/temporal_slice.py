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


class TemporalSlice(ModelNormal):
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
            'item': (bool, date, datetime, dict, float, int, list, str,),
            'value': (bool, date, datetime, dict, float, int, list, str,),
            'type': (str,),
            'duration': (int,),
            'level': (int,),
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'item': 'item',
        'value': 'value',
        'type': 'type',
        'duration': 'duration',
        'level': 'level',
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
        """temporal_slice.TemporalSlice - a model defined in OpenAPI

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
            item (bool, date, datetime, dict, float, int, list, str): The item that was interacted with; for example, in a Jewels game, the  corresponding alphabet, or in a survey, the question index.. [optional]
            value (bool, date, datetime, dict, float, int, list, str): The value of the item that was interacted with; in most games,  this field is  &#x60;null&#x60;, but in a survey, this field is the question  choice index.. [optional]
            type (str): The type of interaction that for this detail; for example, in  a Jewels game,  &#x60;none&#x60; if the tapped jewel was  incorrect, or &#x60;correct&#x60; if it was correct, or in  a  survey, this field will be &#x60;null&#x60;.. [optional]
            duration (int): The time difference from the previous detail or the  start of the parent result.. [optional]
            level (int): The level of activity for this detail; for example, in  games with multiple  levels, this field might be &#x60;2&#x60; or  &#x60;4&#x60;, but for surveys and other games this field  will be &#x60;null&#x60;.. [optional]
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
