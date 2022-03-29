
from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.Head.as_view(), name='head'),
    path('info/', core.views.Info.as_view(), name='info'),
    path('books/', core.views.Books.as_view(), name='book_list'),
    path('books/<int:pk>/', core.views.BookDetail.as_view(), name='book_detail'),
    path('books/create/', core.views.BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/update/', core.views.BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', core.views.BookDelete.as_view(), name='book_delete'),
]
