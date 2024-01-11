from django.http import JsonResponse
from django.conf import settings



def hello(request):
  if settings.DEBUG:
    return JsonResponse({'message': 'DEVMODE Hello, this is a minimal Django API!as'})
  else:
    return JsonResponse({'message': 'PRODMODE Hello, this is a minimal Django API!'})
    
