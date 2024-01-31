"""YG_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from YG.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('user_login',user_login,name="user_login"),
    path('user_signup',user_signup,name="user_signup"),
    path('user_home/',user_home,name="user_home"),
    path('logo_maker/',logo_maker,name="logo_maker"),
    path('business_card/',business_card,name="business_card"),
    path('social/',social,name="social"),
    path('more/',more,name="more"),
    path('make_business_card/',make_business_card,name="make_business_card"),
    path('card_desc/',card_desc,name="card_desc"),
    path('cards/<int:card_id>',card_detail,name="card_detail"),
    path('feedback/',feedback,name="feedback"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
