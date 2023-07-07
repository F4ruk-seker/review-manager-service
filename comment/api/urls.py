from django.urls import path
from comment.api import views


app_name = "comment_api"


urlpatterns = [
    path('', views.CommentSearchListView.as_view(), name='view'),
    path('tag/', views.CommentTagListView.as_view(), name='tags'),
    path('create/', views.CommentCreateView.as_view(), name="create"),
    path('<int:id>/', views.CommentUpdateDestroyRetrieveView.as_view(), name="update_destroy_retrieve"),
]

