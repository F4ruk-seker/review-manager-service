from django.urls import path
from branch.api import views


urlpatterns = [
    # path('all',views.GetUserMainDirectionPost.as_view()  ),
    # path('list', views.GetUserMainDirectionPost.as_view()),
    # path('like/<uuid>', views.GetPostFromUuid.as_view()),
    # path('like/<uuid>', views.GetPostFromUuid.as_view()),
    path('', views.BranchSearchListView.as_view()),
    path('add-metric/', views.BranchMetricCreateView.as_view()),
    path('<id>/', views.BranchCreateUpdateDestroyRetrieveView.as_view()),
    # path('add-branch/', views.BranchCreateView.as_view()),
    # path('remove-branch/', views.BranchMetricCreateView.as_view()),
]
