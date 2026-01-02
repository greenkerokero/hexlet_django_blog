from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.views import View
from django.urls import reverse

from hexlet_django_blog.articles.models import Article
from hexlet_django_blog.articles.forms import ArticleForm

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


# class ArticleIndexView(View):
#     app_config = apps.get_app_config('articles')
#     app_name = app_config.name
# 
#     def get(self, request, *args, **kwargs):
#         return redirect(
#             reverse(
#                 'article_detail',
#                 kwargs={'article_id': 42, 'tags': 'python'}
#             )
#         )


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={
                'articles': articles,
            },
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/article.html',
            context={
                'article': article,
            },
        )


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('articles') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request,
            'articles/update.html',
            {'form': form, 'article_id': article_id},
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article', id=article_id)

        return render(
            request,
            'articles/update.html',
            {'form': form, 'article_id': article_id},
        )


class ArticleFormDeleteView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = get_object_or_404(Article, id=article_id)
        return render(
            request,
            'articles/article_confirm_delete.html',
            context={
                'article': article,
            },
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return redirect('articles')


# def articles_detail(request, article_id=None, tags=None):
#     return render(
#         request,
#         'articles/detail.html', 
#         context={
#             'article_id': article_id,
#             'tags': tags,
#         }
#     )



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
