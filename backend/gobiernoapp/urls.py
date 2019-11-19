from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'regions', views.RegionList, basename="regions")
router.register(r'provinces', views.ProvinceList, basename="provinces")
router.register(r'politicians', views.PoliticianList, basename="politicians")
router.register(r'comments', views.CommentList, basename="comments")

# router.register(r'regionsdetails/(?P<id>\d+)', views.RegionDetail, basename="regionsdetails")
router.register(r'locationpoliticians/(?P<id>\d+)', views.LocationPoliticians, basename="locationpoliticians")

# router.register(r'provincesdetails/(?P<id>\d+)', views.ProvinceDetail, basename="provincesdetails")
router.register(r'regionprovinces/(?P<id>\d+)', views.RegionProvinces, basename="regionprovinces")


router.register(r'politiciansdetails/(?P<id>\d+)', views.PoliticianDetail, basename="politiciansdetails")
router.register(r'commentsdetails/(?P<id>\d+)', views.CommentDetail, basename="commentsdetails")


urlpatterns = [
    path('', include(router.urls)),
]
