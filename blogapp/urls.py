
from django.urls import path

from blogapp.views import BlogView

urlpatterns = [
    path('', BlogView.as_view(), name='listhtml'),
]
