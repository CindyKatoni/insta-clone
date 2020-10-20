from django.urls import path, include
from .views import (
    ProfileListView
)

app_name = 'instagramapp'

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile'),
]