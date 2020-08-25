from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project
from blog.models import Article

# Create your views here.
def index(request):
    projects = Project.objects.all().order_by('priority')
    articles = Article.objects.filter(is_visible=True).order_by('-created_at')[:2]
    template = loader.get_template('portfolio/index.html')
    context = {'projects': projects, 'articles': articles}
    return HttpResponse(template.render(context,request=request))