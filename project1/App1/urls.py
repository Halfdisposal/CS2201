from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    #path('', views.app_view, name='app_view'),
    path('books/<int:pk>/', views.BookDetailView, name='book_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile/', views.accounts_login, name='accounts'),
    path('', views.home, name = 'home')
    # other patterns...
]
