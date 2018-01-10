from astuteclient.common import base

class Invoice(base.Resource):
    """
    """
    def __repr__(self):
        return "<Invoice %s>" % self._info
        
class InvoiceManager(base.Manager):
    """
    """
    resource = Invoice
    
    def list(self):
        """
        """
        path = '/v1/invoice'
        return self._list(path, "")
    
    def get(self):
        """
        """
        path = '/v1/invoice/+' + id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
        
    def create(self):
        """
        """
    def delete(self):
        """
        """