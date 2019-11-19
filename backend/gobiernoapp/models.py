from django.db import models

# Create your models here.

class Region(models.Model):
    reg_name = models.CharField(max_length=500)
    authority = models.CharField(max_length=500)
    def __str__(self):
        return self.reg_name
    class Meta:
        verbose_name_plural = "Regions"
        ordering = ['reg_name']

class Province(models.Model):
    prov_name = models.CharField(max_length=500)
    authority = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    def __str__(self):
        return self.prov_name
    class Meta:
        verbose_name_plural = "Provinces"
        ordering = ['prov_name']

class Politician(models.Model):
    poli_name = models.CharField(max_length=500)
    job = models.CharField(max_length=500)
    location_id = models.IntegerField()
    photo_url = models.CharField(max_length=500)
    def __str__(self):
        return self.poli_name
    class Meta:
        verbose_name_plural = "Politicians"
        ordering = ['id']


class Comment(models.Model):
    comm_content = models.CharField(max_length=500)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    poli_id = models.IntegerField()
    def __str__(self):
        return self.comm_content
    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-id']
