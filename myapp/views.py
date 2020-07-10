from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import person
# Create your views here.

def index(request):
	r = person.objects.all()
	for i in r:
		a = i.name
	context = {'a':a}
	return render(request,'index.html',context)