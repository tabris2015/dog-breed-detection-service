from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Detection
from .utils import get_image_from_data_url
from .services import Predictor
# Create your views here.
def index(request):
    """Pagina de inicio"""
    return render(request, 'detection/index.html')


@csrf_exempt
def receiveImage(request):
    # print(type(request.body))
    predictor = Predictor('tf_models/colab/cats_dogs_best_colab1.h5', 'tf_models/colab/best_colab1_fine.h5')
    img = get_image_from_data_url(request.body)[0]
    res = predictor.predict(img)
    # guardar en la db
    Detection.objects.create(
        date=timezone.now(),
        animal=res['animal'],
        breed=res['raza']['main'])
    print(res)
    return JsonResponse(res)
