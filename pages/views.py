from django.shortcuts import render

# Create your views here.

def home_page_view(request):
  return HttpResponse("Goodbye, World!")
