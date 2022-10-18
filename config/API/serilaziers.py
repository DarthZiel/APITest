from rest_framework import serializers
from .models import Post, User, Mark

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Post
        fields = ("author", "title", "content")

class PostSerializerforList(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Post
        fields = ('author', 'title','content', 'get_count_of_likes', 'get_count_of_dislikes' )

class MarkSerializer(serializers.ModelSerializer):
    user_id = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    post_id = serializers.SlugRelatedField(slug_field='title', queryset=Post.objects.all())
    class Meta:
        model = Mark
        fields = '__all__'


