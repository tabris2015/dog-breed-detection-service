from django.urls import path
from django.http import StreamingHttpResponse
from . import views

from . import services

app_name = 'detection'
urlpatterns = [
    path('', views.index, name='index'),
    path('cv-camera/', lambda r: StreamingHttpResponse(services.gen(services.VideoCamera()),
                                                       content_type='multipart/x-mixed-replace; boundary=frame')),
    path('image/', views.receiveImage, name='receiveImage')
]
