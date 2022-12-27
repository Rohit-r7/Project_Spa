from django.shortcuts import render

# Create your views here.
def commonfun (request) :
    return render (request,'common_templates/common.html')