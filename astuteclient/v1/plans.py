from astuteclient.common import base

class Plan(base.Resource):
    """
    """
    def __repr__(self):
        return "<Plan %s>" % self._info
    
class PlanManager(base.Manager):
    """
    """
    
    def list(self, **kwargs):
        """
        List all the Plans
        """
        url = '/v1/plan'
        qparams = {}
        return self._list(url, "")
    
    def get(self, id):
        """
        """
    
    def create(self):
        """
        """
    
    def delete(self):
        """
        """
        
        
    
