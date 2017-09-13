from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        lookup_field='slug',
        view_name='posts-api:details'
    )

    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'title', 'content', 'draft', 'publish']

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'slug', 'content', 'draft', 'publish']

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'draft', 'publish']
