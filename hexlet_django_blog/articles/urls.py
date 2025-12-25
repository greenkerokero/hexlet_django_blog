from django.urls import path

from hexlet_django_blog.articles import views

urlpatterns = [
    path('', views.ArticleIndexView.as_view(), name='articles'),
    path(
        '<str:tags>/<int:article_id>/',
        views.articles_detail,
        name='article_detail'
    ),
]
