from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_index, name='main'),
    path('signup/', views.signup, name='signup'),
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout')

    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"))
]


