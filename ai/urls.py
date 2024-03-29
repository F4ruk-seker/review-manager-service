from django.contrib import admin
from django.urls import path, include
from ai.views import ai_main, PoolManager, PoolOutput, PoolView, PoolFastTagView

name = 'ai'

urlpatterns = [
    path('', ai_main),
    path('tool/pool/', PoolView.as_view()),
    path('tool/pool/create/', PoolView.as_view()),
    path('tool/pool/<pool_id>/', PoolManager.as_view()),
    path('tool/pool/<pool_id>/output/', PoolOutput.as_view()),
    path('tool/pool/<pool_id>/tag/', PoolOutput.as_view()),
    path('tool/pool/<pool_id>/comment/tag/fast/', PoolFastTagView.as_view()),
]
