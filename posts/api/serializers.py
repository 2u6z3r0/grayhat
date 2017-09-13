from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )


from posts.models import Post

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        lookup_field='slug',
        view_name='posts-api:details'
    )
    author_name = SerializerMethodField()
    class Meta:
        model = Post
        fields = ['url', 'id', 'author_name', 'title', 'content', 'draft', 'publish']

    def get_author_name(self, obj):
        return str(obj.author.get_full_name())


class PostDetailSerializer(ModelSerializer):
    author_name = SerializerMethodField()
    image = SerializerMethodField()
    html_content = SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'author_name', 'title', 'slug', 'content', 'html_content','draft', 'publish', 'image']

    def get_author_name(self, obj):
        return str(obj.author.get_full_name())

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image= None
        return image

    def get_html_content(self, obj):
        return obj.get_markdown()

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'draft', 'publish']
