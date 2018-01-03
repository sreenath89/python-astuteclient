# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
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

from astuteclient.common import utils
import astuteclient.exc as exc


@utils.arg('-m', '--metaquery', metavar='<METAQUERY>',
           help='Query into the metadata metadata.key=value:..')
@utils.arg('-s', '--source', metavar='<SOURCE>',
           help='ID of the resource to show samples for.')
@utils.arg('-r', '--resource_id', metavar='<RESOURCE_ID>',
           help='ID of the resource to show samples for.')
@utils.arg('-u', '--user_id', metavar='<USER_ID>',
           help='ID of the user to show samples for.')
@utils.arg('-p', '--project_id', metavar='<PROJECT_ID>',
           help='ID of the project to show samples for.')
@utils.arg('-c', '--counter_name', metavar='<NAME>',
           help='Name of meter to show samples for.')
@utils.arg('--start', metavar='<START_TIMESTAMP>',
           help='ISO date in UTC which limits events by '
           'timestamp >= this value')
@utils.arg('--end', metavar='<END_TIMESTAMP>',
           help='ISO date in UTC which limits events by '
           'timestamp <= this value')
def do_billing_types():
    """
    """
    print "Sample Billing type"
def do_sample_list(cc, args):
    '''List the samples for this meters.'''
    fields = {'counter_name': args.counter_name,
              'resource_id': args.resource_id,
              'user_id': args.user_id,
              'project_id': args.project_id,
              'source': args.source,
              'start_timestamp': args.start,
              'end_timestamp': args.end,
              'metaquery': args.metaquery}
    try:
        samples = cc.samples.list(**fields)
    except exc.HTTPNotFound:
        raise exc.CommandError('Samples not found: %s' % args.counter_name)
    else:
        field_labels = ['Resource ID', 'Name', 'Type', 'Volume', 'Timestamp']
        fields = ['resource_id', 'counter_name', 'counter_type',
                  'counter_volume', 'timestamp']
        utils.print_list(samples, fields, field_labels,
                         sortby=0)

