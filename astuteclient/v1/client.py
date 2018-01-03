# Copyright Ericsson AB 2014. All rights reserved
#
# Authors: Balazs Gibizer <balazs.gibizer@ericsson.com>
#          Ildiko Vancsa <ildiko.vancsa@ericsson.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import copy

from astuteclient import client as asclient
from astuteclient.openstack.common.apiclient import client
from astuteclient.v2 import meters
from keystoneclient import exceptions

class Client(object):
    """Client for the astute v1 API.

    :param endpoint: A user-supplied endpoint URL for the ceilometer
                            service.
    :type endpoint: string
    :param token: Provides token for authentication.
    :type token: function
    :param timeout: Allows customization of the timeout for client
                    http requests. (optional)
    :type timeout: integer
    """

    def __init__(self, *args, **kwargs):
        print 'dasdsdasdasdsadasdasdas'
        print '====================================='
        """Initialize a new client for the Astute v1 API."""
        self.auth_plugin = kwargs.get('auth_plugin') \
            or asclient.get_auth_plugin(*args, **kwargs)
        self.client = client.HTTPClient(
            auth_plugin=self.auth_plugin,
            region_name=kwargs.get('region_name'),
            endpoint_type=kwargs.get('endpoint_type'),
            original_ip=kwargs.get('original_ip'),
            verify=kwargs.get('verify'),
            cert=kwargs.get('cert'),
            timeout=kwargs.get('timeout'),
            timings=kwargs.get('timings'),
            keyring_saver=kwargs.get('keyring_saver'),
            debug=kwargs.get('debug'),
            user_agent=kwargs.get('user_agent'),
            http=kwargs.get('http')
        )

        self.http_client = client.BaseClient(self.client)
        self.meters = meters.MeterManager(self.http_client)


