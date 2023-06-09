from django.urls import path
from branch.api import views

app_name: str = "branch"

urlpatterns = [
    # path('all',views.GetUserMainDirectionPost.as_view()  ),
    # path('list', views.GetUserMainDirectionPost.as_view()),
    # path('like/<uuid>', views.GetPostFromUuid.as_view()),
    # path('like/<uuid>', views.GetPostFromUuid.as_view()),
    path('', views.BranchSearchListView.as_view()),
    path('create/',views.BranchCreateView.as_view(), name="create"),
    path('add-metric/', views.BranchMetricCreateView.as_view()),
    path('<id>/', views.BranchUpdateDestroyRetrieveView.as_view(), name="update_destroy_retrieve"),
    # path('add-branch/', views.BranchCreateView.as_view()),
    # path('remove-branch/', views.BranchMetricCreateView.as_view()),
]
