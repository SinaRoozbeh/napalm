# Copyright 2015 Spotify AB. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from eos import EOSDriver
from iosxr import IOSXRDriver
from junos import JunOSDriver
from fortios import FortiOSDriver
from ibm import IBMDriver

def get_network_driver(vendor):
    driver_mapping = {
        'EOS': EOSDriver,
        'ARISTA': EOSDriver,
        'IOS-XR': IOSXRDriver,
        'IOSXR': IOSXRDriver,
        'JUNOS': JunOSDriver,
        'JUNIPER': JunOSDriver,
        'FORTIOS': FortiOSDriver,
        'IBM': IBMDriver,
    }
    try:
        return driver_mapping[vendor.upper()]
    except KeyError:
        raise Exception('Vendor/OS not supported: %s' % vendor)

