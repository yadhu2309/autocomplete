from django.shortcuts import render
from .models import Names
from django.http import JsonResponse

# Create your views here.

def get_names(request):
    search = request.GET.get('search')
    names = Names.objects.filter(name__startswith=search)

    payload = []
    for obj in names:
        payload.append({
            'name': obj.name
        })

    return JsonResponse({'status': True, 'payload': payload})

def home(request):
    return render(request,'home.html')
