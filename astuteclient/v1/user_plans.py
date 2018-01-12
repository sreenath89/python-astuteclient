from astuteclient.common import base

class UserPlan(base.Resource):
    """
    """
    def __repr(self):
        return "<UserPlan %s>" % self._info

class UserPlanManager(base.Manager):
    """
    User Plan Manager
    """
    resource_class = UserPlan
    
    def list(self):
        """
        List all the user plans
        """
        path = '/v1/plan/mapping'
        return self._list(path, "")
    
    def get(self, user_plan_mapping_id):
        """
        Get the details of a user plan
        """
        path = '/v1/plan/mapping/' + user_plan_mapping_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
    
    def create(self, plan_id = None, user = None, contract_period = None, quantity = None):
        """
        Create a new user plan
        """
        print('INSIDE PLAN MAPPING CREATE')
        path = '/v1/plan/mapping'
        #body = {"user": user,"contract_period": contract_period,"plans":{plan_id:quantity}}
        #body = {"user": user,"contract_period": contract_period,"plans":{1:1}}
        
        body = {
            "user": user,
            "contract_period": contract_period,
            "plans": {
                plan_id: quantity
            }
        }
        
        print(body)
        return self._create(path, body)
        
    def delete(self):    
        """
        Delete a user plan
        """    
    