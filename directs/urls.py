from django.urls import path
from . import views


urlpatterns = [
    path('inbox', views.inbox, name='inbox'),
    path('directs/<username>', views.Directs, name='directs'),
    path('send/', views.SendMessage, name='send-message'),
    path('new/', views.UserSearch, name='user-search'),
]
