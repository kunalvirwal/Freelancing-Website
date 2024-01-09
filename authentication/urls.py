from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin ,name="signin"),
    
    # path("process_form/", views.process ,name="process"),
]