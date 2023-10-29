from django.shortcuts import render
from rest_framework import generics
from .serializers import CommentSerializer, WriterSerializer
from .models import Comment, Writer

# Create your views here.

class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentEdit(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class WriterList(generics.ListAPIView):
    serializer_class = WriterSerializer
    queryset = Writer.objects.all()

class WriterEdit(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = WriterSerializer
    queryset = Writer.objects.all()
