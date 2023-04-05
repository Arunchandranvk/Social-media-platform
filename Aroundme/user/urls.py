from django.urls import path
from .views import *

urlpatterns=[
    path('home/',Home.as_view(),name="h"),
    path('bio/',BioView.as_view(),name="bio"),
    path('profile/',ProfileView.as_view(),name="profile"),
    path('post/',PostView.as_view(),name="post"),
    path('comment/<int:pid>/',addcomment,name="comment"),
    path('bioupdate/<int:pk>/',BioUpdateView.as_view(),name="bioupd"),
    path('changepassword/',EditPassView.as_view(),name="cpass"),
    path('editpost/<int:pk>/',EditPost.as_view(),name="epost"),
    path('delpost/<int:pk>/',PostDelView.as_view(),name="delpost"),
    path('addlike/<int:pid>/',addlike,name="like"),
  
]