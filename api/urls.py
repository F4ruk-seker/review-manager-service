from django.urls import path, include


urlpatterns = [
    path('branch/', include('branch.api.urls')),
]

