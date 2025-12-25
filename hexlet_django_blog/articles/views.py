from django.shortcuts import render, redirect
from django.apps import apps
from django.views import View
from django.urls import reverse


#class ArticleIndexView(View):
#    def get(self, request, article_id=None, tags=None, *args, **kwargs):
#        if article_id is not None and tags is not None:
#            return render(
#                request,
#                'articles/detail.html', 
#                context={
#                    'article_id': article_id,
#                    'tags': tags,
#                }
#            )
#        else:
#            return redirect(
#                reverse(
#                    'article_detail',
#                    kwargs={'article_id': 'python', 'tags': '42'}
#                )
#            )


class ArticleIndexView(View):
    app_config = apps.get_app_config('articles')
    app_name = app_config.name

    def get(self, request, *args, **kwargs):
        return redirect(
            reverse(
                'article_detail',
                kwargs={'article_id': 42, 'tags': 'python'}
            )
        )


def articles_detail(request, article_id=None, tags=None):
    return render(
        request,
        'articles/detail.html', 
        context={
            'article_id': article_id,
            'tags': tags,
        }
    )



# class ArticleIndexView(View):
#     app_config = apps.get_app_config('articles')
#     app_name = app_config.name
# 
#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             'articles/index.html',
#             context={
#                 'name': self.app_name,
#             }
#         )


# def index(request):
#     app_config = apps.get_app_config('articles')
#     app_name = app_config.name
#     return render(
#         request,
#         'articles/index.html',
#         context={
#             'name': app_name,
#         }
#     )
