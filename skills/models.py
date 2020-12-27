from django.db import models
import uuid


# Create your models here.

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name='name skill', unique=True, blank=False, null=False)
    image = models.ImageField(upload_to='skills/%Y/%m', verbose_name='image of skill', blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Is active?')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Update date')

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('-date_create', )

    def __str__(self):
        return self.name
