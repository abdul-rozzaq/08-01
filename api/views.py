from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Article, Author, Category, Comment
from .serializers import ArticleSerializer, AuthorSerializer, CategorySerializer, CommentSerializer


class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(["GET"])
def home_page(request):
    return Response(
        {
            "categories": "/api/categories/",
            "authors": "/api/authors/",
            "articles": "/api/articles/",
            "comments": "/api/comments/",
        }
    )
