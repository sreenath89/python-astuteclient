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
    
@utils.arg('--plan_id', metavar='<Id of the Plan>', action=NotEmptyAction,
           help='Id of the Plan.')
def do_plan_get(cc, args):
    '''Get the details of a plan'''
    print('Get plan details')
    try:
        print('Inside show billing type functin')
        print(args)
        plan = cc.plans.get(args.plan_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Plan Not Found : %s' %args.plan_id)
    else:
        field_labels = ['Status', 'Code', 'Name', 'Billing Type', 'Rate']
        fields = ['status', 'code', 'name', 'billing_type', 'rate']
        print('before data')
        data = dict((f, getattr(plan, f, '')) for f in fields)
        print('before printing')
        utils.print_dict(data, wrap=72)
    
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
    
@utils.arg('--invoice_id', metavar='<ID of Invoice>', action=NotEmptyAction,
           help='ID of the Invoice whose details are to be shown.')
def do_invoice_get(cc, args):
    '''Get details of a invoice'''
    print('Get Invoice details')
    try:
        print('Inside show invoice function')
        print(args)
        print('-------------After args-----------------')
        invoice = cc.invoices.get(args.invoice_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Invoice Not Found : %s' %args.invoice_id)
    else:
        field_labels = ['Code', 'Date', 'From', 'To', 'User', 'Total', 'Paid Amount', 'Balance']
        fields = ['inv_code', 'inv_date', 'inv_from', 'inv_to', 'user', 'total_amt', 'amt_paid', 'balance_amt']
        print('before data')
        data = dict((f, getattr(invoice, f, '')) for f in fields)
        print('before printing')
        utils.print_dict(data, wrap=72)

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
    
@utils.arg('--discount_type_id', metavar='<ID of Discount Type>', action=NotEmptyAction,
           help='ID of the Discount Type whose details are to be shown.')

def do_discount_type_get(cc, args):
    '''Get the details of a discount type'''
    print('Get discount types')
    try:
        print('Inside show discount type function')
        print(args)
        discount_type = cc.discount_types.get(args.discount_type_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Discount Type Not Found : %s' %args.discount_type_id)
    else:
        field_labels = ['Id', 'Status', 'Code', 'Name']
        fields = ['id', 'status', 'code', 'name']     
        print('before data')
        data = dict((f, getattr(discount_type, f, '')) for f in fields)
        print('before printing')
        utils.print_dict(data, wrap=72)

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
    except exc.HTTPNotFound():
        raise exc.CommandError('Error: No Discounts Found!')
    else:
        field_labels = ['Id', 'Code', 'Name', 'Discount_Type_Id', 'Discount_Type_Code', 'Expiration Date', 'Amt', 'Usage Count']
        fields = ['id', 'code', 'name', 'discount_type_id', 'discount_type_code', 'expiration_date', 'amt', 'usage_count']
        utils.print_list(discounts, fields, field_labels, sortby=0)
    
@utils.arg('--discount_id', metavar='<ID of Discount>', action=NotEmptyAction,
           help='ID of the Discount whose details are to be shown.')
def do_discount_get(cc, args):
    '''Get the details of a individual discount'''
    print('Get discount details')
    try:
        print(args)
        discount = cc.discounts.get(args.discount_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Discount Not Found : %s' %args.discount_id)
    else:
        field_labels = ['Id', 'Code', 'Name', 'Discount_Type_Id', 'Discount_Type_Code', 'Expiration Date', 'Amt', 'Usage Count']
        fields = ['id', 'code', 'name', 'discount_type_id', 'discount_type_code', 'expiration_date', 'amt', 'usage_count']  
        print('before data')
        data = dict((f, getattr(discount, f, '')) for f in fields)
        print('before printing')
        utils.print_dict(data, wrap=72)

def do_discount_create(cc, args):
    '''Create a new discount'''
    print('Create discount')

def do_discount_update(cc, args):
    '''Update the Discount details'''
    print('Update discount details')
    
#################End of Discounts section#################
def do_discount_mappings_list(cc, args):
    '''List all Discount Mappings'''
    try:
        discount_mapping = cc.discount_mappings.list()
    except exc.HTTPNotFound():
        raise exc.CommandError('Error: No Discount Mappings Found!')
    else:
        field_labels = ['Discount_Type_Id', 'Code', 'Name', 'User', 'Apply Type', 'User Plan', 'Discount Id', 'Expiration Date', 'Amt']
        fields = ['discount_type_id', 'code', 'name', 'user', 'apply_type', 'user_plan', 'discount_id' ,'expiration_date', 'amt']
        utils.print_list(discount_mapping, fields, field_labels, sortby=0)

@utils.arg('--discount_mapping_id', metavar='<ID of Discount Mapping>', action=NotEmptyAction,
           help='ID of the Discount Mapping whose details are to be shown.') 
def do_discount_mapping_get(cc, args):
    '''Get the details of an individual Discount Mapping'''
    try:
        print(args)
        discount_mapping = cc.discount_mappings.get(args.discount_mapping_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Error: Discount Mapping Not Found : %s' %args.discount_mapping_id)
    else:
        field_labels = ['Discount_Type_Id', 'Code', 'Name', 'User', 'Apply Type', 'User Plan', 'Discount Id', 'Expiration Date', 'Amt']
        fields = ['discount_type_id', 'code', 'name', 'user', 'apply_type', 'user_plan', 'discount_id' ,'expiration_date', 'amt']  
        data = dict((f, getattr(discount_mapping, f, '')) for f in fields)
        utils.print_dict(data, wrap=72) 

def do_discount_mapping_create(cc, args):
    '''Create a new discount mapping'''
    print('Create a new discount mapping')

def do_discount_mapping_update(cc, args):
    '''Update an existing Discount Mapping'''
    print('Update an existing Discount Mapping')
    
#################End of Discount Mapping section##########
def do_service_types_list(cc, args):
    '''List all service types'''
    try:
        service_types = cc.service_types.list()
    except exc.HTTPNotFound():
        raise exc.CommandError('Error: No Service Types Found!')
    else:
        field_labels = ['Id', 'Name', 'Code', 'Units', 'Status']
        fields = ['id', 'name', 'code', 'units', 'status']
        utils.print_list(service_types, fields, field_labels, sortby=0)
       
@utils.arg('--service_type_id', metavar='<ID of Service Type>', action=NotEmptyAction,
           help='ID of the Service Type whose details are to be shown.') 
def do_service_type_get(cc, args):
    '''Get details of a specific service type'''
    try:
        print(args)
        service_type = cc.service_types.get(args.service_type_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Error: Service Type Not Found : %s' %args.service_type_id)
    else:
        field_labels = ['Id', 'Name', 'Code', 'Units', 'Status']
        fields = ['id', 'name', 'code', 'units', 'status']
        data = dict((f, getattr(service_type, f, '')) for f in fields)
        utils.print_dict(data, wrap=72)   

#################End of Service Types section#############
def do_user_plans_list(cc, args):
    '''List all User Plans'''
    try:
        user_plans = cc.user_plans.list()
    except exc.HTTPNotFound():
        raise exc.CommandError('Error: No User Plans Found!')
    else:
        field_labels = ['Id', 'User', 'Plan Id', 'Status', 'Creation Date', 'Quantity', 'Contract Period']
        fields = ['id', 'user', 'plan_id', 'status', 'created_on', 'qty', 'contract_period']
        utils.print_list(user_plans, fields, field_labels, sortby=0)
       
@utils.arg('--user_plan_id', metavar='<ID of User Plan>', action=NotEmptyAction,
           help='ID of the User Plan whose details are to be shown.') 
def do_user_plan_get(cc, args):
    '''Get details of a specific service type'''
    try:
        print(args)
        user_plan = cc.user_plans.get(args.user_plan_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Error: User Plan Mapping Not Found : %s' %args.user_plan_id)
    else:
        field_labels = ['Id', 'User', 'Plan Id', 'Status', 'Creation Date', 'Quantity', 'Contract Period']
        fields = ['id', 'user', 'plan_id', 'status', 'created_on', 'qty', 'contract_period']
        data = dict((f, getattr(user_plan, f, '')) for f in fields)
        utils.print_dict(data, wrap=72)

#################End of User Plan Mapping section#########
def do_user_billing_type_list(cc, args):
    '''List all User Plans'''
    try:
        user_billing_types = cc.user_billing_types.list()
    except exc.HTTPNotFound():
        raise exc.CommandError('Error: No User Billing Types Found!')
    else:
        field_labels = ['Id', 'User', 'Billing Type', 'Extra Fields']
        fields = ['id', 'user', 'billing_type', 'extra_fields']
        utils.print_list(user_billing_types, fields, field_labels, sortby=0)
       
@utils.arg('--user_billing_type_id', metavar='<ID of User Plan>', action=NotEmptyAction,
           help='ID of the User Plan whose details are to be shown.') 
def do_user_billing_type_get(cc, args):
    '''Get details of a specific service type'''
    try:
        print(args)
        user_billing_type = cc.user_billing_types.get(args.user_billing_type_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Error:User Billing Type Mapping Not Found : %s' %args.user_billing_type_id)
    else:
        field_labels = ['Id', 'User', 'Billing Type', 'Extra Fields']
        fields = ['id', 'user', 'billing_type', 'extra_fields']
        data = dict((f, getattr(user_billing_type, f, '')) for f in fields)
        utils.print_dict(data, wrap=72)

#################End of User Billing Type Mapping section#