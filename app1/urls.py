from django.urls import path
from app1 import views
app_name="app1"

urlpatterns = [
    path("",views.samp,name="samp"),
    path("if/",views.if_demo,name="if"),
    path("ifelse/",views.if_else_demo,name="ifelse"),
    path("for/",views.for_demo,name="for"),
]
