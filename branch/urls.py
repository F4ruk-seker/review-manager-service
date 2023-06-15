from django.urls import path
from branch import views

app_name: str = "branch"

urlpatterns = [
    path('', views.BranchManager.as_view())
]
