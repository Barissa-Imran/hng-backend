from django.urls import path
from server import views

urlpatterns = [
    path('api', views.profile_detail, name='api')
]
