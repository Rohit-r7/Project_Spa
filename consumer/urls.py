from django.urls import path
from . import views
app_name = 'consumer'

urlpatterns = [
   path('' , views.index,name='home'),#home
   path('service',views.service, name='works'), #service
   path('contact',views.contact, name='call') ,#contact
   path('gallery',views.gallery,name='show') , #gallery
   path('reviews',views.reviews,name='testimonials') ,#reviews
   path('suggestions',views.suggestions,name='enchance') , #suggestions
   path('about',views.about,name='history') , #about
   path('aesthetics',views.aesthetics,name='facial')

]

# 'consumer:consumer_index'