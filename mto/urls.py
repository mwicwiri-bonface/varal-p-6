from django.urls import path
from . import views

urlpatterns = [
    path('', views.MtoRegistrationView.as_view(), name="registration"),
]
