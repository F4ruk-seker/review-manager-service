from django.urls import path
from branch.api import views


urlpatterns = [
    # path('all',views.GetUserMainDirectionPost.as_view()  ),
    # path('list', views.GetUserMainDirectionPost.as_view()),
    # path('get/<uuid>', views.GetPostFromUuid.as_view()),
    # path('like/<uuid>', views.GetPostFromUuid.as_view()),
    path('add-branch/', views.BranchCreateView.as_view()),
    path('add-metric/', views.BranchMetricCreateView.as_view()),
]