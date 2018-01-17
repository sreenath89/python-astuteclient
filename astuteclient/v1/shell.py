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
    try:
        billing_types = cc.billing_types.list()
    except exc.HTTPNotFound():
        raise exc.CommandError('Error:No Billing Types Found!')
    else:
        field_labels = ['Id', 'Name', 'Status', 'Code']
        fields = ['id', 'name', 'status', 'code']
        utils.print_list(billing_types, fields, field_labels, sortby=0)

@utils.arg('--billing_type_id', metavar='<ID of Billing Type>', action=NotEmptyAction,
           help='ID of the billing type to show.')
def do_billing_type_get(cc, args):
    '''Display details of a billing type'''
    try:
        billing_type = cc.billing_types.get(args.billing_type_id)
    except exc.HTTPNotFound:
        raise exc.CommandError('Billing Type Not Found : %s' %args.billing_type_id)
    else:
        field_labels = ['Id', 'Name', 'Status', 'Code']
        fields = ['id', 'name', 'status', 'code']
        data = dict((f, getattr(billing_type, f, '')) for f in fields)
        utils.print_dict(data, wrap=72)

@utils.arg(
    '--billing_type_name', 
    metavar='<Billing Type Name>', 
    action=NotEmptyAction,
    help='Name of the Billing Type')

@utils.arg(
    '--billing_type_code', 
    metavar='<Billing Type Code>', 
    action=NotEmptyAction,
    help='Code of the Billing Type')

def do_billing_type_create(cc, args):
    '''Create a new billing type'''
    try:
        bt_create = cc.billing_types.create(args.billing_type_name, args.billing_type_code)
    except Exception, e:
        print(e)
    
@utils.arg(
    '--billing_type_id', 
    metavar='<ID of Billing Type>',
    help='ID of the billing type which is to be updated.')

@utils.arg(
    '--billing_type_name', 
    metavar='<Billing Type Name>', 
    action=NotEmptyAction,
    help='Name of the Billing Type')

@utils.arg(
    '--billing_type_code', 
    metavar='<Billing Type Code>', 
    action=NotEmptyAction,
    help='Code of the Billing Type')

def do_billing_type_update(cc, args):
    '''Update the details of a billing type'''
    try:
        bt_update = cc.billing_types.update(args.billing_type_id, args.billing_type_name, args.billing_type_code)
    except Exception, e:
        print(e)
    else:
        do_billing_type_get(cc, args)

@utils.arg(
    '--billing_type_id', 
    metavar='<ID of Billing Type>',
    help='ID of the billing type which is to be deleted.')

def do_billing_type_delete(cc, args):
    '''Delete a billing type'''
    try:
        cc.billing_types.delete(args.billing_type_id)
    except Exception, e:
        print e
    else:
        do_billing_type_list(cc, args)
    
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
    
@utils.arg(
    '--plan_name', 
    metavar='<Plan Name>', 
    action=NotEmptyAction,
    help='Name of the new plan')

@utils.arg(
    '--plan_code', 
    metavar='<Plan Code>', 
    action=NotEmptyAction,
    help='Code for the Plan')

@utils.arg(
    '--rate', 
    metavar='<Rate>', 
    action=NotEmptyAction,
    help='Rate for the new plan')

@utils.arg(
    '--setup_fee', 
    metavar='<Setup Fee>', 
    action=NotEmptyAction,
    help='Setup Fee for the new plan')

@utils.arg(
    '--billing_type', 
    metavar='<Billing Type>', 
    type = int,
    help='Billing Type of the new plan')

@utils.arg(
    '--ref_id', 
    metavar='<Reference Id>', 
    default=' ',
    help='Ref Id of the new plan')

@utils.arg(
    '--ram', 
    metavar='<Ram>', 
    action=NotEmptyAction,
    help='Ram value of the new plan')

@utils.arg(
    '--cpu', 
    metavar='<Cpu>', 
    action=NotEmptyAction,
    help='Cpu value of the new plan')

@utils.arg(
    '--storage', 
    metavar='<Storage>', 
    action=NotEmptyAction,
    help='Storage value of the new plan')

@utils.arg(
    '--service_type_id', 
    metavar='<Service Type ID>', 
    action=NotEmptyAction,
    help='Service Type for the new plan')
  
def do_plan_create(cc, args):
    '''Create a new plan'''
        
    #Initializing    
    filter_options = {}
    
    print('====================')
    print(args.service_type_id)
    print('SERVICE TYPE ABOVE')
    
    if getattr(args, 'plan_name', None):
        filter_options['plan_name'] = args.plan_name
        
    if getattr(args, 'plan_code', None):
        filter_options['plan_code'] = args.plan_code
        
    if getattr(args, 'rate', None):
        filter_options['rate'] = args.rate
        
    if getattr(args, 'setup_fee', None):
        filter_options['setup_fee'] = args.setup_fee
        
    if getattr(args, 'service_type_id', ""):
        filter_options['service_type_id'] = args.service_type_id
        
    if getattr(args, 'billing_type', None):
        filter_options['billing_type'] = args.billing_type
        
    if getattr(args, 'ref_id', " "):
        filter_options['ref_id'] = args.ref_id
        
    if getattr(args, 'ram', None):
        filter_options['ram'] = args.ram
        
    if getattr(args, 'cpu', None):
        filter_options['cpu'] = args.cpu
        
    if getattr(args, 'storage', None):
        filter_options['storage'] = args.storage
        
    print('====================')
    print(args.service_type_id)
    print('SERVICE TYPE ABOVE')
    
    try:
        print(filter_options)
        print('##########')
        create_plan = cc.plans.create(**filter_options)
    except Exception, e:
        print(e)
    else:
        do_plan_list(cc, args)
    
@utils.arg(
    '--plan_id', 
    metavar='<Id of the Plan>', 
    action=NotEmptyAction,
    help='Id of the Plan.')

def do_plan_delete(cc, args):
    '''Delete a plan'''
    print('Delete plan')
    try:
        cc.plans.delete(args.plan_id)
    except Exception, e:
        print(e)

@utils.arg(
    '--plan_id', 
    metavar='<Id of the Plan>', 
    action=NotEmptyAction,
    help='Id of the Plan.')

@utils.arg(
    '--plan_name', 
    metavar='<Plan Name>', 
    action=NotEmptyAction,
    help='Name of the new plan')

@utils.arg(
    '--plan_code', 
    metavar='<Plan Code>', 
    action=NotEmptyAction,
    help='Code for the Plan')

@utils.arg(
    '--rate', 
    metavar='<Rate>', 
    action=NotEmptyAction,
    help='Rate for the new plan')

@utils.arg(
    '--setup_fee', 
    metavar='<Setup Fee>', 
    action=NotEmptyAction,
    help='Setup Fee for the new plan')

@utils.arg(
    '--billing_type', 
    metavar='<Billing Type>', 
    type = int,
    help='Billing Type of the new plan')

@utils.arg(
    '--ref_id', 
    metavar='<Reference Id>', 
    default=' ',
    help='Ref Id of the new plan')

@utils.arg(
    '--ram', 
    metavar='<Ram>', 
    action=NotEmptyAction,
    help='Ram value of the new plan')

@utils.arg(
    '--cpu', 
    metavar='<Cpu>', 
    action=NotEmptyAction,
    help='Cpu value of the new plan')

@utils.arg(
    '--storage', 
    metavar='<Storage>', 
    action=NotEmptyAction,
    help='Storage value of the new plan')

@utils.arg(
    '--service_type_id', 
    metavar='<Service Type ID>', 
    action=NotEmptyAction,
    help='Service Type for the new plan')

def do_plan_update(cc, args):
    '''Update plan details'''
    print('Update Plan details')
    
    #Initializing
    filter_options = {}
    
    #Fetch the values
    if getattr(args, 'plan_id', None):
        plan_id = args.plan_id
    
    if getattr(args, 'plan_name', None):
        filter_options['plan_name'] = args.plan_name
        
    if getattr(args, 'plan_code', None):
        filter_options['plan_code'] = args.plan_code
        
    if getattr(args, 'rate', None):
        filter_options['rate'] = args.rate
        
    if getattr(args, 'setup_fee', None):
        filter_options['setup_fee'] = args.setup_fee
        
    if getattr(args, 'service_type_id', ""):
        filter_options['service_type_id'] = args.service_type_id
        
    if getattr(args, 'billing_type', None):
        filter_options['billing_type'] = args.billing_type
        
    if getattr(args, 'ref_id', " "):
        filter_options['ref_id'] = args.ref_id
        
    if getattr(args, 'ram', None):
        filter_options['ram'] = args.ram
        
    if getattr(args, 'cpu', None):
        filter_options['cpu'] = args.cpu
        
    if getattr(args, 'storage', None):
        filter_options['storage'] = args.storage
    
    try:
        cc.plans.update(plan_id, **filter_options)
    except Exception, e:
        print(e)
    
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

@utils.arg(
    '--status', 
    metavar='<Discount Type Status>', 
    action=NotEmptyAction,
    help='Status of Discount Type')

@utils.arg(
    '--code', 
    metavar='<Discount Code>', 
    action=NotEmptyAction,
    help='Discount Type Code')

@utils.arg(
    '--name', 
    metavar='<Discount Name>', 
    action=NotEmptyAction,
    help='Name of the Discount Type')
    
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


@utils.arg(
    '--discount_name', 
    metavar='<Discount Name>', 
    help='Name for the Discount')

@utils.arg(
    '--discount_code', 
    action=NotEmptyAction,
    metavar='<Discount Code>', 
    help='Unique Code for the discount')

@utils.arg(
    '--discount_type_id', 
    action=NotEmptyAction,
    metavar='<Type of Discount>', 
    help='Type of Discount')

@utils.arg(
    '--discount_expiry_date', 
    action=NotEmptyAction,
    default = None,
    metavar='<Discount Expiry Date>', 
    help='Expiry date for the discount')

@utils.arg(
    '--discount_amount', 
    action=NotEmptyAction,
    metavar='<Discount Amount>', 
    help='Discount Amount')

@utils.arg(
    '--notes',
    default = "",
    metavar='<Notes>', 
    help='Notes corresponding to the discount')

def do_discount_create(cc, args):
    '''Create a new discount'''

    #Initializing    
    filter_options = {}
    
    if getattr(args, 'discount_name', None):
        filter_options['discount_name'] = args.discount_name
        
    if getattr(args, 'discount_code', None):
        filter_options['discount_code'] = args.discount_code
        
    if getattr(args, 'discount_type_id', None):
        filter_options['discount_type_id'] = args.discount_type_id
        
    if getattr(args, 'discount_expiry_date', ""):
        filter_options['discount_expiry_date'] = args.discount_expiry_date

    if getattr(args, 'discount_amount', None):
        filter_options['discount_amount'] = args.discount_amount
        
    if getattr(args, 'notes', ""):
        filter_options['notes'] = args.notes
    
    try:
        print(filter_options)
        print('##########')
        user_plan_mapping = cc.discounts.create(**filter_options)
    except Exception, e:
        print(e)
    else:
        do_discount_list(cc, args)

@utils.arg(
    '--discount_id', 
    metavar='<ID of Discount>', 
    action=NotEmptyAction,
    help='ID of the Discount whose details are to be updated.')

@utils.arg(
    '--discount_name', 
    metavar='<Discount Name>', 
    help='Name for the Discount')

@utils.arg(
    '--discount_code', 
    action=NotEmptyAction,
    metavar='<Discount Code>', 
    help='Unique Code for the discount')

@utils.arg(
    '--discount_type_id', 
    action=NotEmptyAction,
    metavar='<Type of Discount>', 
    help='Type of Discount')

@utils.arg(
    '--discount_expiry_date', 
    action=NotEmptyAction,
    default = None,
    metavar='<Discount Expiry Date>', 
    help='Expiry date for the discount')

@utils.arg(
    '--discount_amount', 
    action=NotEmptyAction,
    metavar='<Discount Amount>', 
    help='Discount Amount')

@utils.arg(
    '--notes',
    default = "",
    metavar='<Notes>', 
    help='Notes corresponding to the discount')

def do_discount_update(cc, args):
    '''Update the Discount details'''
    
    #Initializing    
    filter_options = {}
    
    if getattr(args, 'discount_id', None):
        filter_options['discount_id'] = args.discount_id
        
    if getattr(args, 'discount_name', None):
        filter_options['discount_name'] = args.discount_name
        
    if getattr(args, 'discount_code', None):
        filter_options['discount_code'] = args.discount_code
        
    if getattr(args, 'discount_type_id', None):
        filter_options['discount_type_id'] = args.discount_type_id
        
    if getattr(args, 'discount_expiry_date', ""):
        filter_options['discount_expiry_date'] = args.discount_expiry_date

    if getattr(args, 'discount_amount', None):
        filter_options['discount_amount'] = args.discount_amount
        
    if getattr(args, 'notes', ""):
        filter_options['notes'] = args.notes
        
    try:
        cc.discounts.update(**filter_options)
    except Exception, e:
        print(e)
  
@utils.arg(
    '--discount_id', 
    metavar='<Discount Id>', 
    help='Id for the Discount')
  
def do_discount_delete(cc, args):
    '''Delete a discount'''
    try:
        discount = cc.discounts.delete(args.discount_id)
    except Exception, e:
        print(e)
        print('Error: Unable to delete the discount!')
    else:
        do_discount_list(cc, args)
    
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

@utils.arg(
    '--discount_mapping_id', 
    metavar='<ID of Discount Mapping>', 
    action=NotEmptyAction,
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

@utils.arg(
    '--discount_type_id', 
    metavar='<ID of Discount Mapping>', 
    type=int,
    help='ID of the Discount Mapping whose details are to be shown.')

@utils.arg(
    '--discount_code', 
    metavar='<Discount Code>', 
    action=NotEmptyAction,
    help='Discount Code')

@utils.arg(
    '--discount_name', 
    metavar='<Discount Name>', 
    action=NotEmptyAction,
    help='Name of the Discount')

@utils.arg(
    '--user', 
    metavar='<Id of the user>', 
    action=NotEmptyAction,
    help='ID of User for whom the discount is to be applied.')

@utils.arg(
    '--apply_type', 
    metavar='<Discount Apply Type>', 
    action=NotEmptyAction,
    help='Discount Apply Time')

@utils.arg(
    '--discount_expiration_date', 
    metavar='<Expiration Date>', 
    action=NotEmptyAction,
    help='Expiration date of Discount Mapping')

@utils.arg(
    '--map_object', 
    metavar='<Map Object>', 
    action=NotEmptyAction,
    help='Map Object corresponding to Discount Mapping')

@utils.arg(
    '--amt', 
    metavar='<Amount>', 
    action=NotEmptyAction,
    help='Amount')

def do_discount_mapping_create(cc, args):
    '''Create a new discount mapping'''
    
    #Initializing    
    filter_options = {}
    
    if getattr(args, 'discount_type_id', None):
        filter_options['discount_type_id'] = args.discount_type_id
        
    if getattr(args, 'discount_name', None):
        filter_options['discount_name'] = args.discount_name
        
    if getattr(args, 'discount_code', None):
        filter_options['discount_code'] = args.discount_code
        
    if getattr(args, 'user', None):
        filter_options['user'] = args.user
    
    if getattr(args, 'apply_type', None):
        filter_options['apply_type'] = args.apply_type
    
    if getattr(args, 'discount_expiration_date', None):
        filter_options['discount_expiration_date'] = args.discount_expiration_date
    
    if getattr(args, 'map_object', None):
        filter_options['map_object'] = args.map_object
    
    if getattr(args, 'amt', None):
        filter_options['amt'] = args.amt

    try:
        cc.discount_mappings.create(**filter_options)
    except Exception, e:
        print(e)
    else:
        do_discount_mappings_list(cc, args)

@utils.arg(
    '--discount_mapping_id', 
    metavar='<ID of Discount Mapping>', 
    type=int,
    help='ID of the Discount Mapping whose details are to be updated.')

@utils.arg(
    '--discount_type_id', 
    metavar='<ID of Discount Mapping>', 
    type=int,
    help='ID of the Discount Mapping whose details are to be shown.')

@utils.arg(
    '--discount_code', 
    metavar='<Discount Code>', 
    action=NotEmptyAction,
    help='Discount Code')

@utils.arg(
    '--discount_name', 
    metavar='<Discount Name>', 
    action=NotEmptyAction,
    help='Name of the Discount')

@utils.arg(
    '--user', 
    metavar='<Id of the user>', 
    action=NotEmptyAction,
    help='ID of User for whom the discount is to be applied.')

@utils.arg(
    '--apply_type', 
    metavar='<Discount Apply Type>', 
    action=NotEmptyAction,
    help='Discount Apply Time')

@utils.arg(
    '--discount_expiration_date', 
    metavar='<Expiration Date>', 
    action=NotEmptyAction,
    help='Expiration date of Discount Mapping')

@utils.arg(
    '--map_object', 
    metavar='<Map Object>', 
    action=NotEmptyAction,
    help='Map Object corresponding to Discount Mapping')

@utils.arg(
    '--amt', 
    metavar='<Amount>', 
    action=NotEmptyAction,
    help='Amount')

def do_discount_mapping_update(cc, args):
    '''Update an existing Discount Mapping'''
    #Initializing    
    filter_options = {}
    
    if getattr(args, 'discount_mapping_id', None):
        filter_options['discount_mapping_id'] = args.discount_mapping_id
        
    if getattr(args, 'discount_type_id', None):
        filter_options['discount_type_id'] = args.discount_type_id
        
    if getattr(args, 'discount_name', None):
        filter_options['discount_name'] = args.discount_name
        
    if getattr(args, 'discount_code', None):
        filter_options['discount_code'] = args.discount_code
        
    if getattr(args, 'user', None):
        filter_options['user'] = args.user
    
    if getattr(args, 'apply_type', None):
        filter_options['apply_type'] = args.apply_type
    
    if getattr(args, 'discount_expiration_date', None):
        filter_options['discount_expiration_date'] = args.discount_expiration_date
    
    if getattr(args, 'map_object', None):
        filter_options['map_object'] = args.map_object
    
    if getattr(args, 'amt', None):
        filter_options['amt'] = args.amt

    try:
        cc.discount_mappings.update(**filter_options)
    except Exception, e:
        print(e)
    else:
        do_discount_mappings_list(cc, args)
    
@utils.arg(
    '--discount_mapping_id', 
    metavar='<Discount Mapping Id>', 
    help='Id of the discount mapping which is to be deleted')

def do_discount_mapping_delete(cc, args):
    '''Delete a Discount Mapping'''
    try:
        cc.discount_mappings.delete(args.discount_mapping_id)
    except Exception, e:
        print(e)
    
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

@utils.arg(
    '--name', 
    metavar='<Name of new Service Type>', 
    action=NotEmptyAction,
    help='Name of the Service Type.')

@utils.arg(
    '--status', 
    metavar='<Code for the newly added Service Type>', 
    action=NotEmptyAction,
    help='Code for the newly Added Service Type')

@utils.arg(
    '--code', 
    metavar='<ID of Service Type>', 
    action=NotEmptyAction,
    help='ID of the Service Type whose details are to be shown.')

@utils.arg(
    '--units', 
    metavar='<Units for the Service Type>',
    default=" ",
    help='Units for the Service Type')

def do_service_type_create(cc, args):
    '''Create a new Service Type'''
    
    #Initializing    
    filter_options = {}

    if getattr(args, 'name', None):
        filter_options['name'] = args.name
        
    if getattr(args, 'status', None):
        filter_options['status'] = args.status
        
    if getattr(args, 'code', None):
        filter_options['code'] = args.code
        
    if getattr(args, 'units', ""):
        filter_options['units'] = args.units

    try:
        create_service_type = cc.service_types.create(**filter_options)
    except Exception, e:
        print(e)
    else:
        do_service_types_list(cc, args)

@utils.arg(
    '--service_type_id', 
    metavar='<ID of Service Type>', 
    action=NotEmptyAction,
    help='ID of the Service Type whose details are to be shown.')
     
@utils.arg(
    '--name', 
    metavar='<Name of new Service Type>', 
    action=NotEmptyAction,
    help='Name of the Service Type.')

@utils.arg(
    '--status', 
    metavar='<Code for the newly added Service Type>', 
    action=NotEmptyAction,
    help='Code for the newly Added Service Type')

@utils.arg(
    '--code', 
    metavar='<ID of Service Type>', 
    action=NotEmptyAction,
    help='ID of the Service Type whose details are to be shown.')

@utils.arg(
    '--units', 
    metavar='<Units for the Service Type>', 
    default = " ",
    help='Units for the Service Type')

def do_service_type_update(cc, args):
    '''Update an existing Service Type'''
    #Initializing    
    filter_options = {}

    if getattr(args, 'service_type_id', None):
        service_type_id = args.service_type_id
        
    if getattr(args, 'name', None):
        filter_options['name'] = args.name
        
    if getattr(args, 'status', None):
        filter_options['status'] = args.status
        
    if getattr(args, 'code', None):
        filter_options['code'] = args.code
        
    if getattr(args, 'units', ""):
        filter_options['units'] = args.units

    try:
        update_service_type = cc.service_types.update(service_type_id, **filter_options)
    except Exception, e:
        print(e)
    else:
        do_service_types_list(cc, args)
    
@utils.arg(
    '--service_type_id', 
    metavar='<ID of Service Type>', 
    action=NotEmptyAction,
    help='ID of the Service Type which is to be deleted.')

def do_service_type_delete(cc, args):
    '''Delete a Service Type'''
    try:
        cc.service_types.delete(args.service_type_id)
    except Exception, e:
        print e
    else:
        do_service_types_list(cc, args)
    

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

@utils.arg(
    '--user', 
    metavar='<User ID>', 
    action=NotEmptyAction,
    help='ID of the User for whom the Plan is to be mapped')

@utils.arg(
    '--contract_period', 
    metavar='<Contract Period>', 
    action=NotEmptyAction,
    help='Contract Period for the Plan')

@utils.arg(
    '--plan_id', 
    type= int,
    metavar='<Plan ID>', 
    help='Plan to be assigned to the user')

@utils.arg(
    '--quantity', 
    type= int,
    metavar='<Quantity>', 
    help='Quantity')

def do_user_plan_create(cc, args):
    '''Assign a plan for the user'''
    
    #Initializing    
    filter_options = {}
    
    if getattr(args, 'user', None):
        filter_options['user'] = args.user
        
    if getattr(args, 'contract_period', None):
        filter_options['contract_period'] = args.contract_period
        
    if getattr(args, 'plan_id', None):
        filter_options['plan_id'] = args.plan_id
        
    if getattr(args, 'quantity', None):
        filter_options['quantity'] = args.quantity
    
    try:
        print(filter_options)
        print('##########')
        user_plan_mapping = cc.user_plans.create(**filter_options)
    except Exception, e:
        print(e)
    else:
        do_user_plans_list(cc, args)
        
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
       

@utils.arg(
    '--user_billing_type_id', 
    metavar='<ID of User Plan>', 
    action=NotEmptyAction,
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

@utils.arg(
    '--billing_type_id', 
    metavar='<Billing Type ID>', 
    action=NotEmptyAction,
    help='ID of the Billing Type which is to be assigned for the user')

@utils.arg(
    '--user', 
    metavar='<User ID', 
    action=NotEmptyAction,
    help='ID of the User for whom the Billing Type is to be mapped')

@utils.arg(
    '--name', 
    default = "",
    metavar='<Name>', 
    help='Name- extra fields')

@utils.arg(
    '--id', 
    default= "",
    metavar='<Id>', 
    help='Id-extra fields')

def do_user_billing_type_create(cc, args):

    #Initializing    
    filter_options = {}
    
    if getattr(args, 'billing_type_id', None):
        filter_options['billing_type_id'] = args.billing_type_id
        
    if getattr(args, 'user', None):
        filter_options['user'] = args.user
        
        
    if getattr(args, 'name', ""):
        filter_options['name'] = args.name
        
    if getattr(args, 'id', ""):
        filter_options['id'] = args.id

    try:
        print(filter_options)
        print('##########')
        user_bt_mapping = cc.user_billing_types.create(**filter_options)
        
    except Exception, e:
        print(e)
    
#################End of User Billing Type Mapping section#

