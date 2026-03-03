from django.urls import path
from rcb.views import *
app_name="something"

urlpatterns = [
    path("captain/",captain,name="captain"),
    path("vicecaptain/",vicecaptain,name="vicecaptain")
]
