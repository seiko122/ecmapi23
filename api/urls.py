from django.urls import path
from .views import NewUser

urlpatterns=[
    path('',NewUser.as_view())
]