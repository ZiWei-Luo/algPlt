from django.urls import path
from probMag import views

urlpatterns = [

    path("insert/", views.insert),
    path("prob/list/", views.prob_list),
    path("delect/", views.delect),
    path("<int:nid>/edit/", views.edit),

]
