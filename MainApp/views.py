from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    # preview=Snippet.objects.filter(id=1)
    return render(request, 'pages/view_snippets.html', context)

def create_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')      
    return render(request, 'add_snippet.html', {'form': form})


def snippet_1(request):
    context = {'pagename': 'сниппет 1'}
    return render(request, 'pages/snippets/1.html', context)

def get_snippets(request):
    snippets = Snippet.objects.filter(hide=False, is_public=True)
    for snippet in snippets:
        snippet.creation_date = snippet.creation_date.strftime("%d/%m/%Y %H:%M")
    context = {"snippets": snippets, "hide": False}
    return render(request, "pages/view_snippets.html", context)

def get_snippets_hidden(request):
    snippets=Snippet.objects.filter(is_public=True)
    for snippet in snippets:
        snippet.creation_date = snippet.creation_date.strftime("%d/%m/%Y %H:%M")
    context = {"snippets": snippets, "hide": True}
    return render(request, "pages/view_snippets.html", context)


def snippet_switch(request, id):
    snippet = Snippet.objects.get(id=id)
    if snippet.hide:
        snippet.hide = False
    else:
        snippet.hide = True
    snippet.save()
    return HttpResponseRedirect("/snippets/list")

def delete_snippet(request, id):
    snippet = Snippet.objects.get(id=id)
    snippet.delete()
    return HttpResponseRedirect("/snippets/list")


def change_snippet(request, id):
    snippet = Snippet.objects.get(id=id)
    snippet.creation_date = snippet.creation_date.strftime("%d/%m/%Y %H:%M")
    context={'snippet': snippet}
    return render(request, 'pages/change_snippet.html')



def change(request):
    snippet = Snippet.objects.get(id=request.POST.get("id"))

    snippet.name = request.POST.get("name")
    snippet.lang = request.POST.get("lang")
    snippet.code = request.POST.get("code")
    snippet.save()
    return HttpResponseRedirect("/snippets/list")