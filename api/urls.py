from django.urls import path, include

app_name = "api"

urlpatterns = [
    path('branch/', include('branch.api.urls', namespace="branch_api")),
]

