from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # 1) Explicitly override logout to allow GET + redirect to 'home'
    path(
        'accounts/logout/',
        LogoutView.as_view(next_page='home'),
        name='logout'
    ),

    # 2) Mount all of Django's built-in auth views under /accounts/
    path('accounts/', include('django.contrib.auth.urls')),

    # 3) Your app's URLs
    path('', include('home.urls')),

    # 4) Admin
    path('admin/', admin.site.urls),
]
