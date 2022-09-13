from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Post
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class PostView(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
