from rest_framework import serializers

from .models import Region, Province, Politician, Comment

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"

class PoliticianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politician
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comm_content', 'likes', 'dislikes']
