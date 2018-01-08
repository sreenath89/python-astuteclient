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
import argparse


class NotEmptyAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        values = values or getattr(namespace, self.dest)
        if not values or values.isspace():
            raise exc.CommandError('%s should not be empty' % self.dest)
        setattr(namespace, self.dest, values)

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
def do_billing_types(cc, args):
    """
    List the billing types
    """

    print('INISDE do_billing_type')
    print('========================')
    print(args)
    print(cc)
    print "Sample Billing type"
    print('BEFORE FETCHING THE DATA')
    billing_types = cc.billing_types.list()
    field_labels = ['Id', 'Name', 'Status', 'Code']
    fields = ['id', 'name', 'status', 'code']
    print('BEFORE PRINTING')
    utils.print_list(billing_types, fields, field_labels, sortby=0)

@utils.arg('--billing_type_id', metavar='<ID of Billing Type>', action=NotEmptyAction,
           help='ID of the billing type to show.')
def do_show_billing_type(cc, args):
    '''Display details of a billing type'''
    try:
        print('Inside show billing type functin')
        print(args)
        billing_type = cc.billing_types.get(args.billing_type_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Billing Type Not Found : %s' %args.billing_type_id)

    field_labels = ['Id', 'Name', 'Status', 'Code']
    fields = ['id', 'name', 'status', 'code']
    print('before data')
    data = dict((f, getattr(billing_type, f, '')) for f in fields)
    print('before printing')
    utils.print_dict(data, wrap=72)


def do_list_plans(cc, args):
    '''List all the available plans'''
    print('Inside do list plans function')
    plans = cc.plans.list()
    field_labels = ['Status', 'Code', 'Name', 'Billing Type', 'Rate']
    fields = ['status', 'code', 'name', 'billing_type', 'rate']
    print('BEFORE PRINTING PLAN LIST')
    utils.print_list(plans, fields, field_labels, sortby=0)
    

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

