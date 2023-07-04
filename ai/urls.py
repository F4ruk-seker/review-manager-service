from django.contrib import admin
from django.urls import path, include
from ai.views import ai_main, pool_manager, PoolOutput, pool_list_view

name = 'ai'

urlpatterns = [
    path('', ai_main),
    path('tools/pool/', pool_list_view),
    path('tools/pool/<pool_id>/', pool_manager),
    path('tools/pool/<pool_id>/output/', PoolOutput.as_view()),
]
