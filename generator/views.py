from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def password(request):
	length = int(request.GET.get('length',9))
	uppercase = request.GET.get('uppercase')
	numbers = request.GET.get('numbers')
	special = request.GET.get('special')
	l = [chr(i) for i in range(ord('a'), ord('z'))]
	if request.GET.get('uppercase'):
		l += [chr(i) for i in range(ord('A'), ord('Z'))]
	if request.GET.get('numbers'):
		l+=list('0123456789')
	if request.GET.get('special'):
		l+= list('@#$%^&*_.')
	thepassword = random.choice([chr(i) for i in range(ord('a'), ord('z'))]) if request.GET.get('uppercase') is None else\
	random.choice([chr(i) for i in range(ord('a'), ord('z'))]+[chr(i).upper() for i in range(ord('a'), ord('z'))])
	random.shuffle(l)
	thepassword+="".join(l[:length-1])
	return render(request, 'generator/password.html', {'password':thepassword, 'uppercase': uppercase, 'numbers':numbers, 'special':special, 'length':length})

def about(request):
	return render(request,'generator/about.html')