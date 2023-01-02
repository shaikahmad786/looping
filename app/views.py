from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'imthiyaz'}
    return render(request,'looping.html',d)