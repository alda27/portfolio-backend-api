# from django.shortcuts import render
from rest_framework import generics
from .serializers import SkillSerializer
from .models import Skill


class ListSkill(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    name = 'skill_list'


class DetailSkill(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    name = 'skill_detail'


