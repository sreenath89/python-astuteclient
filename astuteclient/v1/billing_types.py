from astuteclient.common import base

class BillingType(base.Resource):
    def __init__(self, manager, info, loaded=False):
        _d = {six.u('type_id'): info}
        super(BillingType, self).__init__(manager, _d, loaded)

    def __repr__(self):
        return "<BillingType %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)

class BillingTypeManager(base.Manager):
    """
    Manager Class
    """
    resource_class = BillingType

    def list(self, **kwargs):
        """
        List all the Billing Types
        """
        path = '/billing/type'
        qparams = {}
        return self._list("/v1/billing/type", "billing_types")
    
    def get(self, billing_type):
        """
        Get the details of an individual billing type
        """
        return self._get("/v1/billing/type%s" % base.getid(flavor), "billing_type")
    
    def create(self, name, code):
        """
        Create a New Billing Type
        """
        body = {"name": name, "code":code}
        return self._create("/v1/billing/type", body, "billing_type")
    
    def delete(self, billing_type):
        """
        Delete a billing type
        """
        return self._delete("/v1/billing/type/%s", base.getid(billing_type))

 
