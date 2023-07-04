from django.urls import path
from ai.api import views

app_name: str = "ai_api"

urlpatterns = [
    # path('all',views.GetUserMainDirectionPost.as_view()  ),
    # path('list', views.GetUserMainDirectionPost.as_view()),
    # path('like/<uuid>', views.GetPostFromUuid.as_view()),
    # path('like/<uuid>', views.GetPostFromUuid.as_view()),
    # path('', views.AISearchListView.as_view()),
    # path('create/', views.AICreateView.as_view(), name="create"),
    # # path('metric/', views.AIMetricCreateView.as_view(), name="metric"),
    # path('<id>/', views.AIUpdateDestroyRetrieveView.as_view(), name="update_destroy_retrieve"),
    # path('add-AI/', views.AICreateView.as_view()),
    # path('remove-AI/', views.AIMetricCreateView.as_view()),
    # path('tool/pool/comment/')
    path('tool/pool/', views.PoolListSearchView.as_view()),
    path('tool/pool/<pk>/', views.PoolCommentList.as_view()),
    path('tool/pool/<pool_id>/comment/<comment_id>/', views.PoolCommentAddRemove.as_view())
]
