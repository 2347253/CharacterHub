from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'user']

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['text', 'timestamp', 'user', 'comment_count', 'comments']

    def get_comments(self, obj):
        limit = self.context.get('show_comments', 3)
        comments = Comment.objects.filter(post=obj).order_by('-timestamp')[:limit]
        return CommentSerializer(comments, many=True).data

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()
