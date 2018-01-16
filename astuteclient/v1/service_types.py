from astuteclient.common import base
from lxml import _elementpath

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
        path = "/v1/service_type/%s" % service_type_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
        
    def create(self, name, status, code, units):
        """
        Create a new Service Type
        """
        path = "/v1/service_type"
        body = {
            "name": name,
            "status": status,
            "code": code,
            "units": units
        }
        try:
            return self._create(path, body)
        except Exception, e:
            print(e)
            
    def update(self, service_type_id, name, status, code, units):
        """
        Update a Service Type
        """
        path = "/v1/service_type/%s" % service_type_id
        body = {
            "name": name,
            "status": status,
            "code": code,
            "units": units
        }
        body= {}
        return self._update(path, body)
    
    def delete(self):
        """
        Delete a Service Type
        """
        path = "/v1/service_type/%s" % service_type_id
        try:
            return self._delete(path)
        except Exception, e:
            print(e)
    
        