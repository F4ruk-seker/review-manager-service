from django.urls import path, include

app_name = "api"

urlpatterns = [
    path('branch/', include('branch.api.urls', namespace="branch_api")),
    path('comment/', include('comment.api.urls', namespace="comment_api")),
    path('ai/', include('ai.api.urls', namespace="ai_api")),
]

