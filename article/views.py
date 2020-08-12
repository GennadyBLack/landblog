from django.shortcuts import render, reverse,get_object_or_404,redirect
from django.views import generic
from .models import Article
from .forms import ArticleForm

from django.http import HttpResponseRedirect

def article_detail(request,id):
    article = get_object_or_404(Article,pk=id)
    return render(request,'article-detail.html',context = {'article':article})

class HomePageView(generic.View):

    def get(self, request):
        articles = Article.objects.all().order_by('-date_created')[:10]
        context = {
            'articles':articles,
        }

        return render(request, 'home.html', context)


class AddArticleView(generic.View):

    def get(self, request):

        context = {
            'form':ArticleForm(),
        }

        return render(request, 'add_article.html', context)

    def post(self, request):
        if request.POST:
            form = ArticleForm(request.POST,request.FILES)
            if form.is_valid():
                Article.objects.create(
                    title=form.cleaned_data['title'],
                    body=form.cleaned_data['body'],
                )

                return HttpResponseRedirect(reverse('home_page'))
            else:

                context = {'form':form}
                return render(request, 'add_article.html', context)

