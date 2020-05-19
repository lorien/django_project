from django.urls import path

from board import views

app_name = 'board'
urlpatterns = [
    path('', views.page_home, name='home'),
]
