from django.db import models

# other libraries
import uuid


class Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # I used uuid to make easier the id
    # field
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags'
        ordering = ('-date_created',)

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # I used uuid to make easier the id
    # field
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    url_project_online = models.URLField()  # url of the project online
    url_source_project = models.URLField()  # url of the source code project in github
    image = models.ImageField(upload_to='projects/%Y/%m/%d/', default='projects/default.jpg')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tags, related_name='projects', blank=True)

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'
        ordering = ('-date_created',)

    def __str__(self):
        return self.name
