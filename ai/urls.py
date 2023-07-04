from django.contrib import admin
from django.urls import path, include
from ai.views import ai_main, PoolManager, PoolOutput, PoolView

name = 'ai'

urlpatterns = [
    path('', ai_main),
    path('tools/pool/', PoolView.as_view()),
    path('tools/pool/create/', PoolView.as_view()),
    path('tools/pool/<pool_id>/', PoolManager.as_view()),
    path('tools/pool/<pool_id>/output/', PoolOutput.as_view()),
]
