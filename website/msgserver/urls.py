from django.urls import path
from . import views

urlpatterns = [
        path('get/<int:key>/', views.get_msg, name='key'),
]

