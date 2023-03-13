from django.urls import path
from .views import IndexView, MainView

urlpatterns = [
    path('', IndexView.as_view(), name='login'),
    path('dashboard/<str: username>', MainView.as_view(), name='dashboard')
]