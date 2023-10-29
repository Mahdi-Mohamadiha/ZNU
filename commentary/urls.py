from django.urls import path
from .views import CommentList, CommentEdit, WriterList, WriterEdit

# Create your urls here.

urlpatterns = [
    path('comments/', CommentList.as_view()),
    path('comments/edit/', CommentEdit.as_view()),
    path('writers/', WriterList.as_view()),
    path('writers/edit/', WriterEdit.as_view()),
]