from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from MainApp import views


urlpatterns = [
    path('', views.index_page),
    path('snippets/add', views.add_snippet_page, name="add_snippets"),
    path('snippets/list', views.get_snippets, name="snippets_page"),
    path('snippets/1', views.snippet_1, name="snippet_1"),
    path("snippets/create", views.create_snippet, name='snippet_create'),
    path("snippets/snippet_switch/<int:id>", views.snippet_switch, name="snippet_switch"),
    path("snippets/list_hidden", views.get_snippets_hidden, name="snippets_page_hidden"),
    path("snippets/delete/<int:id>", views.delete_snippet, name="delete_snippet"),
    path("snippets/edit/<int:id>", views.change_snippet, name="change_snippet"),
    path("snippets/change", views.change, name="change"),
    

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
