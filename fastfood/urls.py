from django.urls import path
from .views import product_detail,SavedView,AddRemoveSavedView,delete_product,IndexView,new_comment,delete_comment


urlpatterns = [
    path('',IndexView.as_view(),name='home'),
    path('<int:product_id>/detail',product_detail,name='detail'),
    path('saveds/',SavedView.as_view(),name='saveds'),
    path('addremovesaved/<int:product_id>/',AddRemoveSavedView.as_view(),name='addremovesaved'),
    path('<int:pk>/delete',delete_product,name='delete'),
    path("comment/new", new_comment, name='new_comment'),
    path("comment/<int:comment_id>/delete", delete_comment, name='comment_delete'),
]