from io import BytesIO
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Detection
from .utils import get_image_from_data_url
from .services import Predictor

predictor = Predictor('tf_models/colab/cats_dogs_best_colab1.h5', 'tf_models/colab/best_colab1_fine.h5')


# Create your views here.
def index(request):
    """Pagina de inicio"""
    return render(request, 'detection/index.html')


@csrf_exempt
def receive_image(request):
    img = get_image_from_data_url(request.body)[0]
    res = predictor.predict(img)
    # guardar en la db
    detection = Detection.objects.create(
        date=timezone.now(),
        animal=res['animal'],
        breed=res['raza']['main'])

    # guardar imagen
    img = img.convert('RGB')
    img_file = BytesIO()
    img.save(img_file, 'jpeg')
    img_name = f'{datetime.utcnow()}.jpeg'
    detection.picture.save(
        img_name,
        InMemoryUploadedFile(
            img_file,
            None, '',
            'image/jpeg',
            img.size,
            None
        )
    )
    print(res)
    return JsonResponse(res)
