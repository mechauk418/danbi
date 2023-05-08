from django.urls import path, include
from .views import *

app_name = "accounts"

urlpatterns = [
    path("", User_ViewSet.as_view({'get':'list', 'post':'create'})),
    path("<int:pk>/", User_ViewSet.as_view({'get':'retrieve', "delete": "destroy", "put": "update", "patch": "partial_update"})),
]