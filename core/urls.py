
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('libros/', views.libros, name='libros'),
    path('blog/', views.blog, name='blog'),
    path('tienda/', views.tienda, name='tienda'),
    path('faq/', views.faq, name='faq'),
]
