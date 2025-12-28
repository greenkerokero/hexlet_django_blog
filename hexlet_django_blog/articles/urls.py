from django.urls import path

from hexlet_django_blog.articles import views
from hexlet_django_blog.articles.views import IndexView

urlpatterns = [
    # path('', views.ArticleIndexView.as_view(), name='articles'),
    path("", IndexView.as_view()),
    path(
        '<str:tags>/<int:article_id>/',
        views.articles_detail,
        name='article_detail'
    ),
]
