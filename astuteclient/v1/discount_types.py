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
        List all Discount types
        """
        path = '/v1/discount/type'
        return self._list(path, "")
    
    def get(self, discount_type_id):
        """
        Get the details of an individual discount
        """
        path = "/v1/discount/type/%s" % discount_type_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
    
