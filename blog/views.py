from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Article

# Create your views here.
def home(request):
    articles_list = Article.objects.filter(is_visible=True).order_by('-created_at')

    paginator = Paginator(articles_list, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    template = loader.get_template('blog/home.html')
    context = {'articles': articles, 'paginate': True}
    # message = "bienvenue sur la partie blog"
    # return HttpResponse(message)
    return HttpResponse(template.render(context,request=request))


def post(request, article_url):
    # projects = Project.objects.all().order_by('priority')
    article = Article.objects.get(url=article_url)
    template = loader.get_template('blog/post.html')
    context = {'article': article}
    # message = "bienvenue sur la partie blog"
    # return HttpResponse(message)
    return HttpResponse(template.render(context,request=request))