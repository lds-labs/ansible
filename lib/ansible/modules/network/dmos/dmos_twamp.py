#!/usr/bin/python
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
The module file for dmos_twamp
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'LDS Labs'
}

DOCUMENTATION = """
---
module: dmos_twamp
version_added: 2.9
short_description: 'Manages Two-Way Active Measurement Protocol on DATACOM DmOS devices.'
description:
  - This module provides a declarative management of Two-Way Active Measurement Protocol
    on DATACOM DmOS devices
author: LDS Labs
notes:
  - Tested against DmOS version 5.2.0
  - This module works with connection C(network_cli).
options:
  config:
    description: A list of Two-Way Active Measurement Protocol configurations
    type: list
    elements: dict
    suboptions:
      reflector:
        description: TWAMP reflector configuration
        type: dict
        suboptions:
          admin_status:
            description: The administrative status of the TWAMP reflector
            type: str
            choices:
              - up
              - down
          ipv4:
            description: IPv4 configuration
            type: dict
            suboptions:
              client_address:
                description: White list client address
                type: list
                elements: dict
                suboptions:
                  address:
                    description: Client address
                    type: str
                    required: true
                  state:
                    description: Connection status
                    type: str
                    choices:
                      - enable
                      - disable
              client_network:
                description: White list client network
                type: list
                elements: dict
                suboptions:
                  network:
                    description: Client network
                    type: str
                    required: true
                  state:
                    description: Connection status
                    type: str
                    choices:
                      - enable
                      - disable
          ipv6:
            description: IPv6 configuration
            type: dict
            suboptions:
              client_address:
                description: White list client address
                type: list
                elements: dict
                suboptions:
                  address:
                    description: Client address
                    type: str
                    required: true
                  state:
                    description: Connection status
                    type: str
                    choices:
                      - enable
                      - disable
              client_network:
                description: White list client network
                type: list
                elements: dict
                suboptions:
                  network:
                    description: Client network
                    type: str
                    required: true
                  state:
                    description: Connection status
                    type: str
                    choices:
                      - enable
                      - disable
          port:
            description: <1024-65535> TWAMP Server Port
            type: int
      sender:
        description: TWAMP sender configuration
        type: dict
        suboptions:
          admin_status:
            description: The administrative status of the TWAMP sender
            type: str
            choices:
              - up
              - down
          connection:
            description: TWAMP sender connection configuration
            type: list
            elements: dict
            suboptions:
              id:
                description: TWAMP sender connection ID
                type: int
                required: true
              admin_status:
                description: The administrative status of the TWAMP sender connection
                type: str
                choices:
                  - up
                  - down
              ipv4:
                description: Ipv4 family configuration
                type: dict
                suboptions:
                  source_address:
                    description: TWAMP connection source ip address
                    type: str
                  target_address:
                    description: TWAMP connection target ip address
                    type: str
              ipv6:
                description: Ipv6 family configuration
                type: dict
                suboptions:
                  source_address:
                    description: TWAMP connection source ip address
                    type: str
                  target_address:
                    description: TWAMP connection target ip address
                    type: str
              number_of_packets:
                description: <1-65535> Number of packets sent on every test
                type: int
              server_port:
                description: <1024-65535> Server port number for TCP connection
                type: int
              test_interval:
                description: <0-65535> Test interval in seconds
                type: int
              test_session:
                description: TWAMP sender test-session configuration
                type: list
                elements: dict
                suboptions:
                  id:
                    description: TWAMP sender test-session ID
                    type: int
                    required: true
                  dscp:
                    description: '<0 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 |
                    26 | 28 | 30 | 32 | 34 | 36 | 38 | 40 | 46 | 48 | 56> DSCP value'
                    type: int
                  ipv4:
                    description: Ipv4 family configuration
                    type: dict
                    suboptions:
                      source_address:
                        description: TWAMP test-session source ip address
                        type: str
                      target_address:
                        description: TWAMP test-session target ip address
                        type: str
                  ipv6:
                    description: Ipv6 family configuration
                    type: dict
                    suboptions:
                      source_address:
                        description: TWAMP test-session source ip address
                        type: str
                      target_address:
                        description: TWAMP test-session target ip address
                        type: str
                  max_port:
                    description: <1024-65535> Server maximum port number
                    type: int
                  min_port:
                    description: <1024-65535> Server minimum port number
                    type: int
                  packet_size:
                    description: <64-65535> Packet size value
                    type: int
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
### Using Merged ###

dmos_twamp:
  config:
    - reflector:
        port: 862
        admin_status: up
        ipv4:
          client_address:
            - address: 10.0.0.1
              state: disable
            - address: 10.0.0.2
              state: enable
          client_network:
            - network: 20.0.0.0/24
              state: enable
            - network: 10.0.0.0/24
              state: disable
        ipv6:
          client_address:
            - address: 2018::1
              state: enable
            - address: 2018::2
              state: disable
          client_network:
            - network: 2019::/64
              state: enable
            - network: 2017::/64
              state: disable
      sender:
        admin_status: down
        connection:
          - id: 2
            admin_status: down
            ipv6:
              source_address: 2018::1
              target_address: 2018::2
            number_of_packets: 50
            server_port: 862
            test_interval: 6
            test_session:
              - id: 2
                ipv4:
                  source_address: 10.0.0.1
                  target_address: 10.0.0.2
                max_port: 65535
                min_port: 1024
                dscp: 0
                packet_size: 64
              - id: 3
                ipv6:
                  source_address: 2018::1
                  target_address: 2018::2
          - id: 3
            admin_status: up
            ipv4:
              source_address: 10.0.0.1
              target_address: 10.0.0.2
  state: merged

# This configuration will result in the following commands:

# - oam twamp reflector administrative-status up
# - oam twamp reflector ipv4 client-address 10.0.0.1 disable
# - oam twamp reflector ipv4 client-address 10.0.0.2 enable
# - oam twamp reflector ipv4 client-network 20.0.0.0/24 enable
# - oam twamp reflector ipv4 client-network 10.0.0.0/24 disable
# - oam twamp reflector ipv6 client-address 2018::1 enable
# - oam twamp reflector ipv6 client-address 2018::2 disable
# - oam twamp reflector ipv6 client-network 2019::/64 enable
# - oam twamp reflector ipv6 client-network 2017::/64 disable
# - oam twamp reflector port 862
# - oam twamp sender administrative-status down
# - oam twamp sender connection 3 administrative-status up
# - oam twamp sender connection 3 ipv4 source-address 10.0.0.1
# - oam twamp sender connection 3 ipv4 target-address 10.0.0.2
# - oam twamp sender connection 2 administrative-status down
# - oam twamp sender connection 2 ipv6 source-address 2018::1
# - oam twamp sender connection 2 ipv6 target-address 2018::2
# - oam twamp sender connection 2 number-of-packets 50
# - oam twamp sender connection 2 server-port 862
# - oam twamp sender connection 2 test-interval 6
# - oam twamp sender connection 2 test-session 3 ipv6 source-address 2018::1
# - oam twamp sender connection 2 test-session 3 ipv6 target-address 2018::2
# - oam twamp sender connection 2 test-session 2 ipv4 source-address 10.0.0.1
# - oam twamp sender connection 2 test-session 2 ipv4 target-address 10.0.0.2
# - oam twamp sender connection 2 test-session 2 dscp 0
# - oam twamp sender connection 2 test-session 2 max-port 65535
# - oam twamp sender connection 2 test-session 2 min-port 1024
# - oam twamp sender connection 2 test-session 2 packet-size 64

### Using Delete ###

dmos_twamp:
  config:
    - reflector:
        port: 862
        admin_status: down
        ipv4:
          client_address:
            - address: 10.0.0.1
              state: disable
            - address: 10.0.0.2
          client_network:
            - network: 20.0.0.0/24
              state: enable
            - network: 10.0.0.0/24
        ipv6:
          client_address:
            - address: 2018::1
              state: enable
            - address: 2018::2
          client_network:
            - network: 2017::/64
              state: disable
            - network: 2019::/64
      sender:
        admin_status: down
        connection:
          - id: 2
            number_of_packets: 50
            server_port: 862
            test_interval: 6
            test_session:
              - id: 2
                ipv4:
                  source_address: 10.0.0.1
                  target_address: 10.0.0.2
                max_port: 65535
                min_port: 1024
                dscp: 0
                packet_size: 64
              - id: 3
          - id: 3
  state: deleted

# This configuration will result in the following commands:

# - no oam twamp reflector administrative-status
# - no oam twamp reflector ipv4 client-address 10.0.0.1 disable
# - no oam twamp reflector ipv4 client-address 10.0.0.2
# - no oam twamp reflector ipv4 client-network 20.0.0.0/24 enable
# - no oam twamp reflector ipv4 client-network 10.0.0.0/24
# - no oam twamp reflector ipv6 client-address 2018::1 enable
# - no oam twamp reflector ipv6 client-address 2018::2
# - no oam twamp reflector ipv6 client-network 2019::/64
# - no oam twamp reflector ipv6 client-network 2017::/64 disable
# - no oam twamp reflector port
# - no oam twamp sender administrative-status
# - no oam twamp sender connection 3
# - no oam twamp sender connection 2 number-of-packets
# - no oam twamp sender connection 2 server-port
# - no oam twamp sender connection 2 test-interval
# - no oam twamp sender connection 2 test-session 3
# - no oam twamp sender connection 2 test-session 2 ipv4 source-address
# - no oam twamp sender connection 2 test-session 2 ipv4 target-address
# - no oam twamp sender connection 2 test-session 2 dscp
# - no oam twamp sender connection 2 test-session 2 max-port
# - no oam twamp sender connection 2 test-session 2 min-port
# - no oam twamp sender connection 2 test-session 2 packet-size


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
  changed:
  description: If configuration resulted in any change
  returned: always
  type: bool
  sample: True or False
msg:
  description: Error message
  returned: on error
  type: string
  sample: 'Aborted: reason'
response:
  description: The response of each executed commands
  returned: always
  type: list
  sample: ['Aborted: reason']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.dmos.argspec.twamp.twamp import TwampArgs
from ansible.module_utils.network.dmos.config.twamp.twamp import Twamp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=TwampArgs.argument_spec,
                           supports_check_mode=True)

    result = Twamp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()