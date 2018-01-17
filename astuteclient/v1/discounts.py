from astuteclient.common import base

class Discount(base.Resource):
    """
    """
    def __repr__(self):
        return "<Discount %s>" % self._info

class DiscountManager(base.Manager):
    """
    """
    resource_class = Discount
    
    def list(self):
        """
        """
        path = '/v1/discount'
        return self._list(path, "")
        
    def get(self, discount_id):
        """
        """
        path = '/v1/discount/+' + discount_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
    
    def create(self, discount_name=None, discount_code=None, discount_type_id=None,  discount_expiry_date=None, discount_amount=None, notes=None):
        """
        Create a new Discount
        """
        path = '/v1/discount'
        body = {
            "name": discount_name, 
            "code" : discount_code,
            "discount_type_id" : discount_type_id, 
            "expiration_date" : discount_expiry_date,
            "amt" : discount_amount, 
            "notes" : notes
        }
        return self._create(path, body)
    
    def update(self, discount_id, **kwargs):
        """
        Update a Discount
        """
        path = "/v1/discount/%s" % discount_id
        body = kwargs
        for key in body:
           if body[key] is None:
               body.pop(key)
        try:
            return self._update(path, body)
        except Exception, e:
            print(e)
    
    def delete(self, discount_id = None):
        """
        Delete a Discount
        """
        path = '/v1/discount/' + discount_id
        try:
            return self._delete(path)
        except Exception, e:
            print(e)
            
    
    
        
