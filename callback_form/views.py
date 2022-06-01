from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from .forms import CallbackForm

@csrf_exempt
def callback(request):
    if request.method == "POST":
        Callback = CallbackForm(request.POST)
        if Callback.is_valid():
            Callback.save()
    else:
        Callback = CallbackForm()
    return Response(Callback)
