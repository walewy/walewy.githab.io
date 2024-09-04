from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    name = request.GET.get('name', 'Recruto')
    message = request.GET.get('message', 'Давай дружить')
    response_text = f"Hello {name}! {message}!"
    return HttpResponse(response_text)