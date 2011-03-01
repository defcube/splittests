import random

from django.conf import settings

class AssignSplitTests(object):
    def process_request(self, request):        
        request.splittests = []
        try:
            splittests = settings.SPLITTESTS            
        except AttributeError:
            return
        for key, values in splittests.iteritems():
            key = 'splittest_' + key
            value = request.session.setdefault(key, random.choice(values))
            request.splittests.append((key, value))
            setattr(request, key, value)
            
        
            