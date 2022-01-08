from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):


    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        character.extend(list('!@#$%&*'))
    if request.GET.get('Numbers'):
        character.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(character)

    return render(request, 'generator/password.html', {'password':thepassword})

def aboutme(request):
    return render(request, 'generator/aboutme.html')
