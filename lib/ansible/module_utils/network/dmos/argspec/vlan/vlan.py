#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the dmos_vlan module
"""


class VlanArgs(object):  # pylint: disable=R0903
    """The arg spec for the dmos_vlan module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'elements': 'dict',
            'options': {'interface': {'elements': 'dict',
                                      'options': {'name': {'required': True,
                                                           'type': 'str'},
                                                  'tagged': {'type': 'bool'}},
                                      'type': 'list'},
                        'name': {'type': 'str'},
                        'vlan_id': {'required': True, 'type': 'int'}},
            'type': 'list'},
 'state': {'choices': ['merged', 'replaced', 'overridden', 'deleted'],
           'default': 'merged',
           'type': 'str'}}  # pylint: disable=C0301
