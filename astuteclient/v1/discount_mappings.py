from astuteclient.common import base

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
        path = "/v1/discount/mapping"
        body = {}
        try:
            return self._create(path, body)
        except Exception, e:
            print(e)
    
    def update(self):
        """
        Update a discount mapping
        """
        path = "/v1/discount/mapping"
        body = {}
        try:
            return self._update(path, body)
        except Exception ,e:
            print(e)
        
    def delete(self):
        """
        Delete a discount mapping
        """
        path = "/v1/discount/mapping/" + discount_mapping_id
        try:
            return self._delete(path, body)
        except Exception, e:
            print(e)        
        
        
        
    