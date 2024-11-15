from django.urls import path

from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDestroyAPIView, AuthorAPIView, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, CommentAPIView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("categories/", CategoryListCreateAPIView.as_view(), name="categories-list"),
    path("categories/<int:pk>/", CategoryRetrieveUpdateDestroyAPIView.as_view(), name="categories-retrieve"),
    path("articles/", ArticleListCreateAPIView.as_view(), name="articles-list"),
    path("articles/<int:pk>/", ArticleRetrieveUpdateDestroyAPIView.as_view(), name="articles-retrieve"),
    path("authors/", AuthorAPIView.as_view(), name="authors-list"),
    path("comments/", CommentAPIView.as_view(), name="comments-list"),
]
