from django.urls import path

from hexlet_django_blog.articles.views import (
    IndexView,
    ArticleView,
    ArticleFormCreateView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/', ArticleView.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    # path('', views.ArticleIndexView.as_view(), name='articles'),
    # path(
    #     '<str:tags>/<int:article_id>/',
    #     views.articles_detail,
    #     name='article_detail'
    # ),
]
