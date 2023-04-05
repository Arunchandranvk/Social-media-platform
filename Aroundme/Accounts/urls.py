
from django.urls import path
from .views import *

urlpatterns = [
    path('log/',LogView.as_view(),name="signin"),
    path('Reg/',RegView.as_view(),name="signup"),
    path('logout/',LogOut.as_view(),name="logout"),
    
]
