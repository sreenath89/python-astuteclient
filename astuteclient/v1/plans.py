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
        path = "/v1/plan"
        qparams = {}
        return self._list(path, "")
    
    def get(self, id):
        """
        List the details of an individual plan
        """
        path = "/v1/plan/%s" % id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
    
    def create(self, plan_name, plan_code, rate, setup_fee, 
               service_type_id, billing_type, ref_id, ram, cpu, storage):
        """
        Create a New Plan
        """
        path = "/v1/plan"
        body = {
            "name": plan_name,
            "code": plan_code,
            "rate": rate,
            "setup_fee": setup_fee,
            "service_type": service_type_id,
            "billing_type": billing_type,
            "ref_id": ref_id,
            "attrs":{
                "ram": ram,
                "cpu": cpu,
                "storage": storage
            }
        }
        print('CREAAAAAAATE')
        print(body)
        return self._create(path, body)
    
    def delete(self, plan_id):
        """
        Delete a Plan
        """
        path = "/v1/plan/%s" % plan_id
        try:
            return self._delete(path)
        except Exception, e:
            print(e)
    
    def update(self, plan_id, **kwargs):
        """
        Update a Plan
        """
        path = "/v1/plan/%s" % plan_id
        body = kwargs
#       for key in body:
#            if body[key] is None:
#                body.pop(key)

        print('####ABOVE BODY####')
        print body
        print('####BELOW BODY####')
        
        if kwargs['ram']:
            body['attrs']['ram'] = kwargs['ram']
        if kwargs['cpu']:
            body['attrs']['cpu'] = kwargs['cpu']
        if kwargs['storage']:
            body['attrs']['storage'] = kwargs['storage']
            
        try:
            return self._update(path, body)
        except Exception, e:
            print(e)

