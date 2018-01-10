from astuteclient.common import base

class Plan(base.Resource):
    """
    """
    def __repr__(self):
        return "<Plan %s>" % self._info
    
class PlanManager(base.Manager):
    """
    """
    resource_class = Plan
    
    def list(self, **kwargs):
        """
        List all the Plans
        """
        path = '/v1/plan'
        qparams = {}
        return self._list(path, "")
    
    def get(self, id):
        """
        List the details of an individual plan
        """
        path = '/v1/plan/' + id
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
        
        
    
