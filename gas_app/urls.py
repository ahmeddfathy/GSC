from django.urls import path
from . import views
urlpatterns = [
     path('',views.home,name='home'),
     path('ecommere',views.ecommere,name='ecommere'),
     path('support',views.support,name='support'),
     path('chatbot',views.chatbot,name='chatbot'),
   
 
   
    
]

# myapp/urls.py
