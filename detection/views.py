from django.shortcuts import render

# Create your views here.
def index(request):
    """Pagina de inicio"""
    return render(request, 'detection/index.html')

