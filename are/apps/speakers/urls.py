from django.urls import path
from . import views

urlpatterns = [
   path('speaker/',views.ViewSpeaker.as_view(),name='speaker'),
]    

