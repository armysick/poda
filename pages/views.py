from django.shortcuts import render

# Create your views here.

def home_page_view(request):
  if 'good' in 'feeling good':
    return HttpResponse("Hello, World!")
  else:
    return HttpResponse("Goodbye, World!")


