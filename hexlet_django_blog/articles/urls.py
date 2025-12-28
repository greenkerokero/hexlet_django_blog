from django.urls import path

from hexlet_django_blog.articles import views
from hexlet_django_blog.articles.views import IndexView, ArticleView

urlpatterns = [
    path('', IndexView.as_view()),
    path("<int:id>/", ArticleView.as_view()),
    # path('', views.ArticleIndexView.as_view(), name='articles'),
    #path(
    #    '<str:tags>/<int:article_id>/',
    #    views.articles_detail,
    #    name='article_detail'
    #),
]
