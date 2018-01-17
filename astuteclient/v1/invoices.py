from astuteclient.common import base

class Invoice(base.Resource):
    """
    """
    def __repr__(self):
        return "<Invoice %s>" % self._info
        
class InvoiceManager(base.Manager):
    """
    """
    resource_class = Invoice
    
    def list(self):
        """
        """
        path = '/v1/invoice'
        return self._list(path, "")
    
    def get(self, invoice_id):
        """
        """
        path = '/v1/invoice/+' + invoice_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
        
#     def create(self):
#         """
#         """
#         path = "/v1/invoice"
#         body = {}
#         try:
#             return self._create(path, body)
#         except Exception, e:
#             print(e)
            
    def delete(self):
        """
        """
        path = "/v1/invoice/" + invoice_id
        try:
            return self._delete(path)
        except Exception, e:
            print(e)
    
    def update(self, invoice_id):
        """
        Update an Invoice
        """
        path = "/v1/invoice/" + invoice_id
        body = {}
        try:
            return self._update(invoice_id)
        except Exception, e:
            print(e)
