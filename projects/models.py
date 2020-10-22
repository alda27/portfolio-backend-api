from django.db import models

# other libraries
import uuid


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # I used uuid to make easier the id
    # field
    name = models.CharField(max_length=200)
    description = models.TextField()
    url_project_online = models.URLField()  # url of the project online
    url_source_project = models.URLField()  # url of the source code project in github
    image = models.ImageField(upload_to='projects/%Y/%m/%d/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # I used uuid to make easier the id
    # field
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    projects = models.ManyToManyField(Project, related_name='tags', blank=True, null=True)
