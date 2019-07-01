"""RBACpython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rbac import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^login', views.login),
    url(r'^index', views.index),
    url(r'^logout', views.logout),
    # url(r'^default', views.default),
    url(r'^user_info', views.userinfo),
    url(r'^user_list', views.userlist),
    url(r'^role_list', views.role_list),
    url(r'^per_list', views.per_list),
    url(r'^del/(\d)/', views.delete),
    url(r'^safe_set', views.safe_set),
    url(r'^myperssion', views.myperssion)
]
