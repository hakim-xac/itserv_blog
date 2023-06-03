from django.urls import path, include
from . import views
from .views import PostView


urlpatterns = [
    path('', PostView.as_view(), name='post_list'),
]