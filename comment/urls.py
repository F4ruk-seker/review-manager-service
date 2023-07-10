from django.urls import path, include
from comment.views import *


app_name = "comment"

urlpatterns = [
    path('', CommentSearchListView.as_view(), name="comment_list"),
    path('fast/', FastTagView.as_view(), name="comment_fast"),
]

