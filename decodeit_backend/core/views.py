from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import User
# Create your views here.
@csrf_exempt

def save(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        name = data.get('name')
        avatar = data.get('avatar')
        language = data.get('language')
        score = data.get('score')
        User.objects.create(name=name, avatar=avatar, language=language, score=score)
        return JsonResponse({'message': 'Data saved successfully'})

def index(request):
    return render(request, 'index.html')     
    
