import random

from django.conf import settings

class AssignSplitTests(object):
    def process_request(self, request):        
        request.splittests = []
        try:
            splittests = settings.SPLITTESTS            
        except AttributeError:
            return
        if not splittests:
            return
        for key, values in splittests.iteritems():
            self._set_splittest_value(key, request, values)

    def _set_splittest_value(self, key, request, values):
        key = 'splittest_' + key
        if request.GET.has_key('clearsplit'):
            value = self._pick_new_value(values, request, key)
        else:
            value = request.session.setdefault(key, random.choice(values))
            if value not in values:
                value = self._pick_new_value(values, request, key)
        request.splittests.append((key, value))
        setattr(request, key, value)

    def _pick_new_value(self, values, request, key):
        value = random.choice(values)
        request.session[key] = value
        return value
            
        
            