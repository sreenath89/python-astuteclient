from astute.common import base

class ServiceType(base.Resource):
    """
    """
    def __repr__(self):
        return "<ServiceType %s>" % self._info

class ServiceTypeManager(base.Manager):
    """
    Service Type Manager Class
    """
    resource_class = ServiceType
    
    def list(self):
        """
        """
        path = "/v1/service_type"
        return self._list(path, "")
    
    def get(self, service_type_id):
        """
        """
        path = "/v1/service_type/" + service_type_id
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
    
        