from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'draft', 'publish']

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'draft', 'publish']

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'draft', 'publish']
