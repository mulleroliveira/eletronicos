from django.urls import path
from . import views

urlpatterns = [
    path('', views.computador_list),
    path('detalhes/<int:computador_id>/', views.computador_show),
    path('form/', views.computador_form),
    path('delete/<int:computador_id>/', views.computador_delete)
]