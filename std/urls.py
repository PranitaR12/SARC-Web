
from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("home/", home),
    path("add-std/", std_add),
    path("delete-std/<int:event>", delete_std),
    path("update-std/<int:event>", update_std),
    path("do-update-std/<int:event>", do_update_std),
]

