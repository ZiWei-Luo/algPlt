"""
URL configuration for algPlt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from algMag import views

urlpatterns = [

    # 用户管理
    path("user/login/", views.user_login),
    path("user/insert/", views.user_insert),
    path("user/delect/", views.user_delect),
    path("user/list/", views.user_list),
    path("user/<int:nid>/update/", views.user_update),

    #问题实例管理
    path("prob/insert/", views.prob_insert),
    path("prob/delect/", views.prob_delect),
    path("prob/list/", views.prob_list),
    path("prob/<int:nid>/update/", views.prob_update),

    #算法管理
    path("alg/insert/", views.alg_insert),
    path("alg/delect/", views.alg_delect),
    path("alg/list/", views.alg_list),
    path("alg/<int:nid>/update/", views.alg_update),
    path("alg/select/<str:ids>", views.alg_list),

    #参数管理
    path("para/<int:nid>/insert/", views.para_insert),
    path("para/delect/", views.para_delect),
    path("para/<int:nid>/list/", views.para_list),
    path("para/<int:nid>/update/", views.para_update),

    #执行方案管理
    path("plan/insert/", views.plan_insert),
    path("plan/delect/", views.plan_delect),
    path("plan/list/", views.plan_list),
    path("plan/<int:nid>/update/", views.plan_update),
    path("plan/exe/", views.plan_exe),


    #结果展示
    path("res/Res/",views.res_Res),
    path("res/lineChart/",views.res_lineChart),
    path("res/boxChart/",views.res_boxChart),





]
