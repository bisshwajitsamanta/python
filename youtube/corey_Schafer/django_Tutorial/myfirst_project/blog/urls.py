from . import views
from django.urls import path

urlpatterns = [
    path("", views.home,name='blog-home'),
    path("about/", views.about,name='blog-about'),
    path("vlog/", views.vlog_about,name='vlog-page'),
]