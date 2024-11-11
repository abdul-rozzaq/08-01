from django.urls import path

from .views import ArticleAPIView, AuthorAPIView, CategoryAPIView, CommentAPIView, home_page

urlpatterns = [
    path("", home_page),
    path("categories/", CategoryAPIView.as_view()),
    path("authors/", AuthorAPIView.as_view()),
    path("articles/", ArticleAPIView.as_view()),
    path("comments/", CommentAPIView.as_view()),
]
