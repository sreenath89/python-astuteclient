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

def do_billing_type_list(cc, args):
    """
    List the billing types
    """
    print('INISDE do_billing_type')
    print('========================')
    print(args)
    print(cc)
    print "Sample Billing type"
    print('BEFORE FETCHING THE DATA')
    try:
        billing_types = cc.billing_types.list()
    except exc.HTTPNotFound():
        raise exc.CommandError('Error:No Billing Types Found!')
    else:
        field_labels = ['Id', 'Name', 'Status', 'Code']
        fields = ['id', 'name', 'status', 'code']
        print('BEFORE PRINTING')
        utils.print_list(billing_types, fields, field_labels, sortby=0)

@utils.arg('--billing_type_id', metavar='<ID of Billing Type>', action=NotEmptyAction,
           help='ID of the billing type to show.')
def do_billing_type_get(cc, args):
    '''Display details of a billing type'''
    try:
        print('Inside show billing type functin')
        print(args)
        billing_type = cc.billing_types.get(args.billing_type_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Billing Type Not Found : %s' %args.billing_type_id)
    else:
        field_labels = ['Id', 'Name', 'Status', 'Code']
        fields = ['id', 'name', 'status', 'code']
        print('before data')
        data = dict((f, getattr(billing_type, f, '')) for f in fields)
        print('before printing')
        utils.print_dict(data, wrap=72)

def do_billing_type_create(cc, args):
    '''Create a new billing type'''
    
def do_billing_type_update(cc, args):
    '''Update the details of a billing type'''

def do_billing_type_delete(cc, args):
    '''Delete a billing type'''
    

def do_plan_list(cc, args):
    '''List all the available plans'''
    try:
        print('Inside do list plans function')
        plans = cc.plans.list()
    except exc.HTTPNotFound():
        raise exc.CommandError('Error:No Plans Found!')
    else:
        field_labels = ['Status', 'Code', 'Name', 'Billing Type', 'Rate']
        fields = ['status', 'code', 'name', 'billing_type', 'rate']
        print('BEFORE PRINTING PLAN LIST')
        utils.print_list(plans, fields, field_labels, sortby=0)
    
def do_plan_get(cc,args):
    '''Get the details of a plan'''
    print('Get plan details')
    
def do_plan_create(cc, args):
    '''Create a new plan'''
    print('Create a new plan')
    
def do_plan_delete(cc, args):
    '''Delete a plan'''
    print('Delete plan')

def do_plan_update(cc, args):
    '''Update plan details'''
    print('Update Plan details')
    
#################End of Plan section#################
def do_invoice_list(cc, args):
    '''List Invoices'''
    try:
        invoices = cc.invoices.list()
    except exc.HTTPNotFound():
        raise exc.CommandError('Error: No Invoices Found!')
    else:
        field_labels = ['Code', 'Date', 'From', 'To', 'User', 'Total', 'Paid Amount', 'Balance']
        fields = ['inv_code', 'inv_date', 'inv_from', 'inv_to', 'user', 'total_amt', 'amt_paid', 'balance_amt']
        utils.print_list(invoices, fields, field_labels, sortby=0)
    
def do_invoice_get(cc, args):
    '''Get details of a invoice'''
    print('Get Invoice details')

#################End of Invoices section#################
def do_discount_type_list(cc, args):
    '''List all Discount Types'''
    try:
        discount_types = cc.discount_types.list()
    except exc.HTTPNotFound():
        raise exc.CommandError('Error: No Discount Types Found!')
    else:
        field_labels = ['Id', 'Status', 'Code', 'Name']
        fields = ['id', 'status', 'code', 'name']
        utils.print_list(discount_types, fields, field_labels, sortby=0)
    
def do_discount_type_get(cc, args):
    '''Get the details of a discount type'''
    print('Get discount types')

def do_discount_type_create(cc, args):
    '''Create a new discount type'''
    print('Create new discount type')

def do_discount_type_update(cc, args):
    '''Update the details of a discount type'''
    print('Update discount type details')
    
#################End of Discount Types Section#################
def do_discount_list(cc, args):
    '''List all discounts'''
    try:
        discounts = cc.discounts.list()
    except exc.test_HTTPNotFound():
        raise exc.CommandError('Error: No Discounts Found!')
    else:
        field_labels = ['Id', 'Code', 'Name', 'Discount_Type_Id', 'Discount_Type_Code', 'Expiration Date', 'Amt', 'Usage Count']
        fields = ['id', 'code', 'name', 'discount_type_id', 'discount_type_code', 'expiration_date', 'amt', 'usage_count']
        utils.print_list(discounts, fields, field_labels, sortby=0)
    
def do_discount_get(cc, args):
    '''Get the details of a individual discount'''
    print('Get discount details')

def do_discount_create(cc, args):
    '''Create a new discount'''
    print('Create discount')

def do_discount_update(cc, args):
    '''Update the Discount details'''
    print('Update discount details')
    
#################End of Discounts section#################