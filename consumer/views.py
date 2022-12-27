from django.shortcuts import render

# Create your views here.
def index (request) :
    return render (request,'consumer_templates/index.html')

def service (request) :
    return render (request,'consumer_templates/services.html')

def contact (request) :
    return render (request,'consumer_templates/contact.html')

def gallery (request) :
    return render (request,'consumer_templates/gallery.html')

def reviews (request) :
    return render (request,'consumer_templates/reviews.html')

def suggestions (request) :
    return render (request,'consumer_templates/suggestions.html')

def about (request) :
    return render (request,'consumer_templates/about.html')

def aesthetics (request) :
    return render (request,'consumer_templates/aesthetics.html')