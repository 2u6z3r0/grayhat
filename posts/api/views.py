from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
    )
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

from .pagination import PostPageNumberPagination
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
    permission_classes = [IsAdminUser, IsOwnerOrReadOnly]

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter]
    SearchFields = ['title', 'content', 'author__first_name', 'author__last_name']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.active()
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset_list = Post.objects.all()

        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query)
            )
        return queryset_list



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