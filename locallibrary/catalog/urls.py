from django.urls import path
from . import views


#the name parameter is included here so that we can refer to this URL mapping in other parts of the code
#for when we want to create links to this page in our templates
#it would look like: {% url 'index' %}
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), 
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    #<int:pk> is a path converter that matches an integer and passes it to the view as a variable called pk
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    
]
