from django.urls import path

from cats.views import cat_add_or_list, cat_edit_or_delete

urlpatterns = [
   path('cats/', cat_add_or_list),
   path('cats/<int:pk>/', cat_edit_or_delete),
]
