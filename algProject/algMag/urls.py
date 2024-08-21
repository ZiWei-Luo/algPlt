from django.urls import path
from algMag import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("pram/<int:nid>/insert/", views.pram_insert),
    path("alg/insert/", views.alg_insert),
    path("alg/list/", views.alg_list),
    path("pram/<int:nid>/list/", views.parm_list),
    path("alg/delect/", views.alg_delect),
    path("pram/delect/", views.pram_delect),
    path("alg/<int:nid>/update/", views.alg_update),
    path("pram/<int:nid>/update/", views.pram_update),

]
