from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [    
    path('', views.main_page, name='index'),
    path(r'blog/', views.main_page, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]