from django.urls import path
from .views import page_detail

urlpatterns = [
    path('<slug>/', page_detail, name='page_detail'),
]
