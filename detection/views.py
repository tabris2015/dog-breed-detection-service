from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import get_image_from_data_url
# Create your views here.
def index(request):
    """Pagina de inicio"""
    return render(request, 'detection/index.html')

@csrf_exempt
def receiveImage(request):
    # print(type(request.body))
    image_file = get_image_from_data_url(request.body)[0]
    print(type(image_file))
    return HttpResponse(status=200)
