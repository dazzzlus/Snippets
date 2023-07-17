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
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
