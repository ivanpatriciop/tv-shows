from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.main),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:show_id>', views.read),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/destroy', views.destroy),
    path('shows/update/<int:show_id>', views.update),
    
    
]
