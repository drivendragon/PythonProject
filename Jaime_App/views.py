from django.shortcuts import render, HttpResponse

# Create your views here.
#from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return HttpResponse("/")

def show(request):
    return HttpResponse("placeholder to display blog number: {number}" )

def edit(request):
    return HttpResponse("placeholder to edit blog {number}")

def destroy(request):
    return HttpResponse("/")