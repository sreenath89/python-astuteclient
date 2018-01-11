from astuteclient.common import base

class BillingType(base.Resource):
    def __repr__(self):
        return "<BillingType %s>" % self._info

class BillingTypeManager(base.Manager):
    """
    Manager Class
    """
    resource_class = BillingType

    print('INSIDE BILINGTYPEMANAGER CLASS')

    def list(self, **kwargs):
        """
        List all the Billing Types
        """
        url = '/v1/billing/type'
        qparams = {}
        return self._list(url, "")

    
    def get(self, id):
        """
        Get the details of an individual billing type
        """
        #path = self._get("/v1/billing/type" + id)
        path = "/v1/billing/type/" + id

        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
    
    def create(self, name, code):
        """
        Create a New Billing Type
        """
        body = {"name": name, "code":code}
        return self._create("/v1/billing/type", body, "")
    
    def delete(self, billing_type):
        """
        Delete a billing type
        """
        return self._delete("/v1/billing/type/%s", base.getid(billing_type))

 
