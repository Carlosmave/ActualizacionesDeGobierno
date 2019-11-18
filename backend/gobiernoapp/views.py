from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Region, Politician, Comment
from django.contrib import messages
import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegionSerializer, PoliticianSerializer, CommentSerializer
from rest_framework import generics, viewsets, mixins

# Create your views here.

class RegionList(viewsets.ReadOnlyModelViewSet): #RegionListViewSet
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class PoliticianList(viewsets.ReadOnlyModelViewSet): #RegionListViewSet
    queryset = Politician.objects.all()
    serializer_class = PoliticianSerializer

class CommentList(viewsets.ReadOnlyModelViewSet): #RegionListViewSet
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RegionDetail(viewsets.ReadOnlyModelViewSet):  #RegionDetailViewSet
    serializer_class = PoliticianSerializer
    def get_queryset(self):
       id = self.kwargs['id']
       region = Region.objects.get(id=id)
       return Politician.objects.all().filter(region=region.reg_name)


class PoliticianDetail(viewsets.ModelViewSet): #PoliticianViewSet
    serializer_class = CommentSerializer
    def get_queryset(self):
       id = self.kwargs['id']
       return Comment.objects.all().filter(poli_id=id)
    def perform_create(self, serializer):
        # The request politician is set as owner automatically.
        serializer.save(poli_id=self.kwargs['id'])


#Funciona para listar y actualizar

class CommentDetail(viewsets.ModelViewSet): #CommentDetailViewSet
    serializer_class = CommentSerializer
    http_method_names = ['get', 'patch']
    def get_queryset(self):
       id = self.kwargs['id']
       return Comment.objects.all().filter(id=id)
    def get_object(self):
       id = self.kwargs['id']
       return Comment.objects.get(id=id)
    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


# class CommentDetail(viewsets.ModelViewSet): #CommentDetailViewSet
#     serializer_class = CommentSerializer
#     def get_queryset(self):
#        id = self.kwargs['id']
#        return Comment.objects.get(id=id)

       #return Comment.objects.all().filter(id=id)
    # def get_object(self):
    #    id = self.kwargs['id']
    #    return Comment.objects.get(id=id)

    # def patch(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)


#Funciona para listar pero no actualizar
# class CommentDetail(viewsets.ModelViewSet): #CommentDetailViewSet
#     serializer_class = CommentSerializer
#     def get_queryset(self):
#        id = self.kwargs['id']
#        return Comment.objects.all().filter(id=id)
#     def perform_create(self, serializer):
#         # The request politician is set as owner automatically.
#         serializer.save(poli_id=self.kwargs['id'])







#---------------------------------------------------------------------------------------------------------------------------------------------------------


def regionindex(request):
    if (request.method == 'POST' and 'buscarregion' in request.POST):
        buscar=request.POST.get('buscar', '')
        regions=Region.objects.all().filter(reg_name__icontains=buscar)
        context = {'regions':regions}
        return render(request, 'gobiernoapp/regionindex.html', context)
    else:
        regions=Region.objects.all()
        context = {'regions':regions}
        return render(request, 'gobiernoapp/regionindex.html', context)


def regiondetails(request, id):
    region = Region.objects.get(id=id)
    politicians=Politician.objects.all().filter(region=region.reg_name)
    context = {'region':region, 'politicians':politicians}
    return render(request, 'gobiernoapp/regionsdetails.html', context)


def politiciandetails(request, id):
    if (request.method == 'POST' and 'createcomment' in request.POST):
        comment=request.POST.get('comment', '')
        comment_obj = Comment(comm_content=comment, poli_id=id)
        comment_obj.save()
        return HttpResponseRedirect('/politiciansdetails/'+str(id))
    else:
        politician = Politician.objects.get(id=id)
        comments=Comment.objects.all().filter(poli_id=id)
        context = {'politician':politician, 'comments':comments}
        return render(request, 'gobiernoapp/politiciansdetails.html', context)


def likesupdates(request, id, cid):
    comment = Comment.objects.get(id=cid)
    comment.likes = comment.likes+1
    comment.save()
    return HttpResponseRedirect('/politiciansdetails/'+str(id))


def dislikesupdates(request, id, cid):
    comment = Comment.objects.get(id=cid)
    comment.dislikes = comment.dislikes+1
    comment.save()
    return HttpResponseRedirect('/politiciansdetails/'+str(id))
