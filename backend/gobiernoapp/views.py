from .models import Region, Politician, Comment
from .serializers import RegionSerializer, PoliticianSerializer, CommentSerializer
from rest_framework import viewsets

# Create your views here.

class RegionList(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class PoliticianList(viewsets.ReadOnlyModelViewSet):
    queryset = Politician.objects.all()
    serializer_class = PoliticianSerializer

class CommentList(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RegionDetail(viewsets.ReadOnlyModelViewSet):
    serializer_class = PoliticianSerializer
    def get_queryset(self):
       id = self.kwargs['id']
       region = Region.objects.get(id=id)
       return Politician.objects.all().filter(region=region.reg_name)


class PoliticianDetail(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    def get_queryset(self):
       id = self.kwargs['id']
       return Comment.objects.all().filter(poli_id=id)
    def perform_create(self, serializer):
        serializer.save(poli_id=self.kwargs['id'])
        

class CommentDetail(viewsets.ModelViewSet):
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
