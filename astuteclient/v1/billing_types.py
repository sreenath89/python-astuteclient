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
        path = '/v1/billing/type'
        qparams = {}
        return self._list(path, "")

    
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
        path = "/v/billing/type"
        body = {"name": name, "code":code}
        return self._create(path, body)
    
    def update(self, name, code):
        """
        Update a Billing Type
        """
        path = "/v1/billing/type"
        try:
            return self._update(path, body)
        except Exception, e:
            print(e)
    
    def delete(self, billing_type_id):
        """
        Delete a billing type
        """
        path = "/v1/billing/type" + billing_type_id
        try:
            return self._delete(path)
        except Exception, e:
            print(e)
            

 
