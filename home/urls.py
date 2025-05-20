from django.urls import path
from .views import home, signup, entry_create

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('create/', entry_create, name='entry_create'),
]