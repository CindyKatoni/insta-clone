from django.shortcuts import render
from .models import Profile
from django.views.generic import (
    ListView
)

# Create your views here.

class ProfileListView(ListView):
    template_name = "instagram/profile.html"
    queryset = Profile.objects.all()
    context_object_name = 'profiles'