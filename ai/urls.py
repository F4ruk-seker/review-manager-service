from django.contrib import admin
from django.urls import path, include
from ai.views import ai_main, pool_manager

urlpatterns = [
    path('', ai_main),
    path('tools/pool/', pool_manager),
]
