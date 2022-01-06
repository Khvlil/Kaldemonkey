from django.urls import path
from . import views


urlpatterns = [
    path('', views.interface, name='interface' ),
        path('home/', views.home, name='home' ),

    path('panda/', views.panda, name='panda'),
        path('django/', views.django, name='django'),
            path('tkinter/', views.tkinter, name='tkinter'),
                path('flask/', views.flask, name='flask')
]
