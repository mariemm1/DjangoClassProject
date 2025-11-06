
from django.urls import path

from blogapp.views import BlogCreateWithFields, BlogCreateWithForm, BlogView, blogDeleteView, blogUpdateView
app_name='Posts'
urlpatterns = [
    path('', BlogView.as_view(), name='listhtml'),
    path('create', BlogCreateWithFields.as_view(), name='createhtml'),
    path('create2', BlogCreateWithForm.as_view(), name='createhtml'),

    path('update/<int:id>', blogUpdateView.as_view(), name='updatehtml'),
    path('delete/<int:id>', blogDeleteView.as_view(), name='deletehtml'),



]
