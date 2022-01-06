from django.conf import settings
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('login/', views.loginpage, name='login'),
         path('logout/',  LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),  name='logout'),

]
