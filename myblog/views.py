from django.shortcuts import render
from models import Article
from django.http import HttpRequest
# Create your views here.

def index(req):
    Arts = Article.objects.all()
    return render(req, 'myblog/index.html',{'Arts':Arts})

def show(req,id):
    Art = Article.objects.get(pk=id)
    return render(req, 'myblog/show.html',{'Art':Art})

def edit(req):
    return render(req,'myblog/edit.html')

def editAction(req):
    tit = req.POST.get('title')
    con = req.POST.get('content')
    Article.objects.create(title = tit,content = con)
    Arts = Article.objects.all()
    return render(req,'myblog/index.html', {'Arts': Arts})

def change(req,id):
    art = Article.objects.get(pk=id)
    return render(req,'myblog/change.html',{'art':art})

def changeAction(req,id):
    tit = req.POST.get('title')
    con = req.POST.get('content')
    art = Article.objects.get(pk=id)
    art.title = tit
    art.content = con
    art.save()

    return render(req, 'myblog/show.html', {'Art':art})