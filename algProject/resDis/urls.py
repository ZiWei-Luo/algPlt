from django.urls import path
from resDis import views


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("algRes/",views.algRes),
    path("algRes/lineChart/",views.lineChart),
    path("algRes/boxChart/",views.boxChart),


]