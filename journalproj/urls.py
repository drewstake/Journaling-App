from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', include('django.contrib.auth.urls')),      # keep login, password URLs
    path('accounts/logout/',                                         
         LogoutView.as_view(next_page='home'),                      # ← override here
         name='logout'),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]