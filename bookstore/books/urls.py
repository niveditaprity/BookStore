

from django.urls import path
from .views import BookListView,BookDetailView
from . import views
urlpatterns = [
    path('books',BookListView.as_view()),
    path('books/<int:pk>',BookDetailView.as_view(),name='books.id'),
    path('books/<int:id>/review',views.review,name='books.review'),
    path('<str:author>',views.author,name='author.books')
]