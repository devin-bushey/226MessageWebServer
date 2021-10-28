from django.urls import path
from . import views

urlpatterns = [
        path('get/<str:key>/', views.get_msg, name='key'),
        path('create/', views.MessageCreate.as_view(), name='message_create'),
        path('update/<str:pk>/', views.MessageUpdate.as_view(), name='message_update'),
        path('', views.get_all_messages, name='messages'),
]

