from django.urls import path
from .views import recipe_create, recipe_delete, recipe_detail, recipe_list, recipe_update
urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipe/new/', recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit', recipe_update, name='recipe_update'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
]