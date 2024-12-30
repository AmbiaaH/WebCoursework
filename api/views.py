from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#This Main page should be accessed after the user is logged in
@login_required
def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def login(request):
    return render(request, 'api/spa/login.html',{})

def register(request):
    return render(request, 'api/spa/register.html',{})