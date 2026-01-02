from django.urls import path

from hexlet_django_blog.articles.views import (
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormEditView,
    ArticleFormDeleteView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    path(
        '<int:id>/edit/',
         ArticleFormEditView.as_view(),
         name='articles_update',
    ),
    path(
        '<int:id>/delete/',
        ArticleFormDeleteView.as_view(),
        name='articles_delete',
    ),
    path('<int:id>/', ArticleView.as_view(), name='article'),

    # path('', views.ArticleIndexView.as_view(), name='articles'),
    # path(
    #     '<str:tags>/<int:article_id>/',
    #     views.articles_detail,
    #     name='article_detail'
    # ),
]
