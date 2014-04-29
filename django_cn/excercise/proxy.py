from django.contrib.auth.models import User
from excercise.models import ProxyUser

class ProxyUserMiddleware():
    def process_request(self, request):
        try: 
            proxyUser = ProxyUser.objects.get(pk=request.user.pk)
            request.proxyUser = proxyUser
        except:
            request.proxyUser = '' 
