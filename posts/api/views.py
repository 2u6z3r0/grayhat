from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    )

from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer,
    )

from posts.models import Post
from rest_framework.permissions import (
    IsAdminUser, AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    )

from .permissions import IsOwnerOrReadOnly

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    lookup_field = 'slug'

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [IsOwnerOrReadOnly]

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [IsAuthenticated, IsAdminUser]