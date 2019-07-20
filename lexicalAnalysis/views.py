from django.shortcuts import render
from django.http import HttpResponse
from pyhanlp import *
# Create your views here.
def lexicalAnalysis(request):
	if(request.method == 'POST'):
		inputm = request.POST.get('a', 0)
	else :
		inputm = u"请输入中文"
	ans = HanLP.segment(str(inputm))
	return render(request, 'lexicalAnalysis.html', {"ans":ans,"inputtext": inputm})
def home(request):
	return render(request, 'base.html')
