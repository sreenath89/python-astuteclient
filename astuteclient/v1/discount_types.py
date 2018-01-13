from astuteclient.common import base

class DiscountType(base.Resource):
    """
    """
    def __repr__(self):
        return "<DiscountType %s>" % self._info
    
class DiscountTypeManager(base.Manager):
    """
    """
    resource_class = DiscountType

    def list(self, **kwargs):
        """
        """
        path = '/v1/discount/type'
        return self._list(path, "")
    
    def get(self, discount_type_id):
        """
        """
        path = '/v1/discount/type/' + discount_type_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
        
    def create(self, status, code, id, name):
        """
        Create a new Discount Type
        """
        path = "/v1/discount/type"
        body = {
            "status": status,
            "code": code,
            "id": id,
            "name": name 
        }
        return self._create(path, body)
        
        
    def delete(self):
        """
        """
