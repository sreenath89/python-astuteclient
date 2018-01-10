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
    
    def create(self):
        """
        """
    
    def delete(self):
        """
        """
        
