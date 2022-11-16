"""abcbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#=> 생성한 모든 앱 가져오기!
urlpatterns = [
    path('admin/', admin.site.urls),
    # 페이지 메인
    path('', include('homepage.urls')),
    path('chart/', include('chart.urls')),
    path('exchange/', include('exchange.urls')),
    path('history/', include('history.urls')),
    path('users/', include('users.urls'))
]