from django.urls import path
from comment.api import views
from ai.api.views import FastTag as ft_ai

app_name = "comment_api"


urlpatterns = [
    path('', views.CommentSearchListView.as_view(), name='view'),
    path('tag/', views.CommentTagListView.as_view(), name='tags'),
    path('create/', views.CommentCreateView.as_view(), name="create"),
    path('fast/', ft_ai.as_view(), name="fast"),
    path('pass/<int:id>/', views.CommentPass.as_view(), name="fast"),
    path('stat/', views.StatView.as_view(), name="stat"),
    path('<int:id>/', views.CommentUpdateDestroyRetrieveView.as_view(), name="update_destroy_retrieve"),
]

