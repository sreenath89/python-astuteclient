from astuteclient.common import base

class UserBillingType(base.Resource):
    """
    """
    def __repr__(self):
        return "<UserBillingType %s>" % self._info

class UserBillingTypeManager(base.Manager):
    """
    """
    resource_class = UserBillingType
    
    def list(self):
        """
        List all user billing types
        """
        path = "/v1/billing/mapping"
        return self._list(path, "")
    
    
    def get(self, mapping_id):
        """
        Get the details of a specific user billing type mapping
        """
        path = "/v1/billing/mapping/" + mapping_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
        
        
    def create(self, billing_type_id = None, user_id = None, name = "", id=""):
        """
        Create a new user-billing type mapping
        """
        path = "/v1/billing/mapping"
        
        #Creating the body of the contents to be passed for creating the new mapping
        body = {
            "billing_type": billing_type_id,
            "user": user_id,
            "extra_fields": {
                "name": name,
                "id": id
            }
        }
        return self._create(path, body)
        
    
    def delete(self):
        """
        Delete a user-billing type mapping
        """
        
        