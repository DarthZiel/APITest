from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Post, Mark
from .serilaziers import PostSerializer, MarkSerializer,PostSerializerforList
# Create your views here.
class PostListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializerforList

class CreatePostAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SetMarkAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MarkSerializer


class UpdateMarkAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
