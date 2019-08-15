from django.urls import path, include
from BlogManager import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home/', views.HomeView.as_view(), name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('list/', views.ListView.as_view(), name='list'),
    path('drafts/', views.DraftsView.as_view(), name='drafts'),
    path('post/', views.DraftsView.as_view(), name='post'),
]
