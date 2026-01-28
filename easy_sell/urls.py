from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('bucket/', include('bucket.urls')),
]
