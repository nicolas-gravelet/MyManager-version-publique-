"""personalServer URL Configuration

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
from django.urls import include, path
from medias.views import MediaViewSet
from career.views import OffreViewSet
from rent.views import LocationViewSet, ParamsViewSet
from rest_framework.routers import DefaultRouter

medias_list = MediaViewSet.as_view({"get": "list"})
medias_detail = MediaViewSet.as_view(
    {"get": "retrieve", "put": "update",
        "patch": "partial_update", "delete": "destroy"}
)
offre_list = OffreViewSet.as_view({"get": "list"})
offre_detail = OffreViewSet.as_view(
    {"get": "retrieve", "put": "update",
        "patch": "partial_update", "delete": "destroy"}
)
location_list = LocationViewSet.as_view({"get": "list"})
location_detail = LocationViewSet.as_view(
    {"get": "retrieve", "put": "update",
        "patch": "partial_update", "delete": "destroy"}
)
locparam_list = ParamsViewSet.as_view({"get": "list"})
locparam_detail = ParamsViewSet.as_view(
    {"get": "retrieve", "put": "update",
        "patch": "partial_update", "delete": "destroy"}
)

router = DefaultRouter()
router.register(r"medias", MediaViewSet, basename="medias")
router.register(r"career", OffreViewSet, basename="career")
router.register(r"rent", LocationViewSet, basename="rent")
router.register(r"locparams", ParamsViewSet, basename="locparams")

urlpatterns = [
    path("", include(router.urls)),
    path("medias/", medias_list, name="media-list"),
    path("medias/<int:pk>/", medias_detail, name="media-detail"),
    path("career/", offre_list, name="offres-list"),
    path("career/<int:pk>/", offre_detail, name="offres-detail"),
    path("rents/", location_list, name="locations-list"),
    path("rents/<int:pk>/", location_detail, name="locations-detail"),
    path("rents-params/", locparam_list, name="locparam-list"),
    path("rents-params/<int:pk>/", locparam_detail, name="locparam-detail"),
]
