from astuteclient import client as astute_client
from os import environ as env

# kwargs for connection
kwargs = {
    "username":    env['OS_USERNAME'],
    "password":    env['OS_PASSWORD'],
    "tenant_name": env['OS_TENANT_NAME'],
    "auth_url":    env['OS_AUTH_URL'],
    "region_name": env['OS_REGION_NAME'],
    "endpoint":    'http://198.100.181.74:9080/',
    "insecure":    False
}

#Connection
astute = astute_client.Client('1', **kwargs)

#print "###LISTING PLANS###"
#plans = astute.plans.list()
#print plans

#print "###LISTING DISCOUNTS###"
#discounts = astute.discounts.list()
#print discounts

#print "###LIST SERVICE TYPES###"
#service_types = astute.service_types.list()
#print service_types

#print "###LIST DISCOUNT TYPES###"
#discount_types = astute.discount_types.list()
#print discount_types

#print "###GET DISCOUNT TYPE DETAILS###"
#discount_type_details = astute.discount_types.get(1)
#print discount_type_details

#print "###LIST INVOICES###"
#invoice_list = astute.invoices.list()
#print invoice_list

#print "###GEt INVOICE DETAILS###"
#invoice_details = astute.invoices.get(1)
#print invoice_details

#print "###LIST BILLING TYPES##"
#billing_types = astute.billing_types.list()
#print billing_types

#print "###GET BILLING TYPE DETAILS###"
#billing_type = astute.billing_types.get(1)
#print billing_type

#print "###LIST USER PLANS###"
#user_plans = astute.user_plans.list()
#print user_plans

#print "###GET USER PLAN DETAILS###"
#user_plan = astute.user_plans.get(1)
#print user_plan

#print "###LIST USER BILLING TYPES###"
#user_billing_types = astute.user_billing_types.list()
#print user_billing_types

#print "###GET USER BILLING TYPE DETAILS###"
#user_billing_type = astute.user_billing_types.get(1)
#print user_billing_type

#print "###LIST DISCOUNT MAPPINGS###"
#discount_mappings = astute.discount_mappings.list()
#print discount_mappings

#print "###GET DISCOUNT MAPPING DETAILS###"
#discount_mapping = astute.discount_mappings.get(1)
#print discount_mapping



