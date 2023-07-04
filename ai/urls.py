from django.contrib import admin
from django.urls import path, include
from ai.views import ai_main, pool_manager, PoolOutput

name = 'ai'

urlpatterns = [
    path('', ai_main),
    path('tools/pool/<pool_id>/', pool_manager),
    path('tools/pool/<pool_id>/output/', PoolOutput.as_view()),
]
