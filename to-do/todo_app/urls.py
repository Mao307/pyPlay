from django.urls import path
from . import views

urlpatterns= [
    path("", views.ListListView.as_view(), name ="index"),
    path("list/<int:list_id>/",views.ItemListView.as_view(), name ="list"),
    path("list/add", views.ListCreate.as_view(), name = "List-add"),
    path("List/<int:List_id>/item/add/", views.ItemCreate.as_view(), name = "item_id",),
    path("List/<int:list_id>/item/update", views.ItemUpdate.as_view(), name = "item_update",)

]