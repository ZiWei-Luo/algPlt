from django.urls import path
from userMag import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("login/", views.login),
    path("insert/", views.insert),
    path("delect/", views.delect),
    path("select/", views.select),
    path("update", views.update),
    path("select/list/", views.select_list),
    path("<int:nid>/edit/", views.edit),
]
