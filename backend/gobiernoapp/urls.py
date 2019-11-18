from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     url(r'^regions/', views.regionindex, name='regionindex'),
#     url(r'^regionsdetails/(?P<id>\d+)/$', views.regiondetails, name='regiondetails'),
#     url(r'^politiciansdetails/(?P<id>\d+)/$', views.politiciandetails, name='politiciandetails'),
#     url(r'^politiciansdetails/(?P<id>\d+)/likes/(?P<cid>\d+)$', views.likesupdates, name='likesupdates'),
#     url(r'^politiciansdetails/(?P<id>\d+)/dislikes/(?P<cid>\d+)$', views.dislikesupdates, name='dislikesupdates'),
#
#
#     url(r'^api/regions$', views.RegionList.as_view()),
#     url(r'^api/regionsdetails/(?P<id>\d+)/$', views.RegionDetail.as_view()),
#     url(r'^api/politiciansdetails/(?P<id>\d+)/$', views.PoliticianDetail.as_view()),
# ];


######################
# region_list = RegionList.as_view({
#     'get': 'list',
# })
# regions_details = RegionDetails.as_view({
#     'get': 'list',
# })
# politicians_details = PoliticianDetail.as_view({
#     'get': 'retrieve',
#     'patch': 'partial_update',
# })
#
#
# urlpatterns = [
#     path('regions/', views.regionindex, name='regionindex'),
#     path('regionsdetails/<int:id>/', views.regiondetails, name='regiondetails'),
#     path('politiciansdetails/<int:id>/', views.politiciandetails, name='politiciandetails'),
#     path('politiciansdetails/<int:id>/likes/<int:cid>/', views.likesupdates, name='likesupdates'),
#     path('politiciansdetails/<int:id>/dislikes/<int:cid>/', views.dislikesupdates, name='dislikesupdates'),
#
#
#     path('api/regions', region_list, name='region-list'),
#     path('api/regionsdetails/<int:id>/', regions_details, name='regions-details'),
#     path('api/politiciansdetails/<int:id>/', politicians_details, name='politicians-details'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

router = DefaultRouter()
router.register(r'regions', views.RegionList, basename="regions")
router.register(r'politicians', views.PoliticianList, basename="politicians")
router.register(r'comments', views.CommentList, basename="comments")

router.register(r'regionsdetails/(?P<id>\d+)', views.RegionDetail, basename="regionsdetails")
router.register(r'politiciansdetails/(?P<id>\d+)', views.PoliticianDetail, basename="politiciansdetails")
router.register(r'commentsdetails/(?P<id>\d+)', views.CommentDetail, basename="commentsdetails")

 #url(r'^api/regionsdetails/(?P<id>\d+)/$', views.RegionDetail.as_view()),
#router.register(r'comments', views.PoliticianDetail)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
