from rest_framework import serializers

from api.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["pk", "title", "link", "creation_date", "up_votes", "author_name"]
        extra_kwargs = {
            "title": {"required": True, "allow_blank": False},
            "link": {"required": True, "allow_blank": False},
            "author_name": {"required": True, "allow_blank": False},
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "pk",
            "content",
            "author_name",
            "creation_date",
        ]
        extra_kwargs = {
            "content": {"required": True, "allow_blank": False},
            "author_name": {"required": True, "allow_blank": False},
        }
