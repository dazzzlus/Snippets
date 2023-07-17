from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.forms import SnippetForm
from .models import Snippet

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()    
        context = {'pagename': 'Добавление нового сниппета', 'form':form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method=='POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")
        return render(request, 'pages/add_snippet.html', {'form': form})


def snippets_page(request):
    context = {'pagename': 'Просмотр сниппетов'}
    preview=Snippet.objects.filter(id=1)
    return render(request, 'pages/view_snippets.html', context)

def create_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('redirect_url')       ###################temporary
    return render(request, 'add_snippet.html', {'form': form})


def snippet_1(request):
    context = {'pagename': 'сниппет 1'}
    return render(request, 'pages/snippets/1.html', context)

def get_snippets(request):
    snippets = Snippet.objects.filter(hide=False, is_public=True)
    for item in snippets:
        item.creation_date = item.creation_date.strftime("%Y-%m-%d %H:%M")
    context = {"snippets": snippets, "hide": False}
    return render(request, "pages/view_snippets.html", context)