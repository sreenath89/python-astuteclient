from astute.common import base

class DiscountMapping(base.Resource):
    """
    """
    def __repr__(self):
        return "<DiscountMapping %s>" % self._info

class DiscountMappingManager(base.Manager):
    """
    Discount Mapping Manager
    """
    resource_class = DiscountMapping
    
    def list(self):
        """
        List all discount mappings
        """
        path = '/v1/discount/mapping'
        return self._list(path, "")
    
    def get(self, discount_mapping_id):
        """
        Get details of a discount mapping
        """
        path = "/v1/discount/mapping/" + discount_mapping_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
    
    def create(self):
        """
        Create a discount mapping
        """
    def delete(self):
        """
        Delete a discount mapping
        """
        
        
        
        
    