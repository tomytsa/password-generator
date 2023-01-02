from django.shortcuts import render
import random 
from django.http import HttpResponse
import string
# Create your views here.
def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request,'generator/home.html')

def password(request):
    abecedario_mayus = string.ascii_uppercase
    abecedario_minus = string.ascii_lowercase
    characters = list(abecedario_minus)
    generated_password = ""
    
  

    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list(abecedario_mayus))
    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))


    for x in range(length):
        generated_password += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': generated_password})    

def about(request):
    return render(request, 'generator/about.html')

