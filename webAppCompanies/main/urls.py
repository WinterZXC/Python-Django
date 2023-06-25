from django.urls import path
from . import views
from .views import CapitalAddView, CapitalCreateView

urlpatterns = [
    path('', views.index, name="main"),
    path("searchName/", views.search_name, name="search_name"),
    path("searchCompanie/", views.search_companie, name="search_companie"),
    path('companies/<int:id>/', views.detail_page, name="detail"),
    path('create/', CapitalCreateView.as_view(), name="create"),
    path('add/<int:id>/', CapitalAddView.as_view(), name="add_capital")
]