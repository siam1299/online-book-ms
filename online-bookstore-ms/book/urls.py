from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views

urlpatterns = [
  path('search/', views.search, name='search'),
  path('book-details/<int:pk>', views.book_details, name='book_details'),
]


