from django.urls import path
from branch import views

app_name: str = "branch"

urlpatterns = [
    path('', views.BranchListView.as_view()),
    path('<branch_id>/', views.BranchManager.as_view())
]
