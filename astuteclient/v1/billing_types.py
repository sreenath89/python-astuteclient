from astuteclient.common import base

class BillingType(base.Resource):
    def __init__(self, manager, info, loaded=False):
        _d = {six.u('type_id'): info}
        super(BillingType, self).__init__(manager, _d, loaded)

    def __repr__(self):
        return "<BillingType %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)

class BillingTypeManager(base.Manager):
    """
    """
    resource_class = BillingType

    def list(self, **kwargs):
        path = '/billing/type'

        return self._list('/v1%s' % path, 'billing_types')
