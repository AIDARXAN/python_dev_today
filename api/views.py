from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Post, Comment
from api.serializers import PostSerializer, CommentSerializer


@api_view()
def ping(request):
    return Response({"message": "Pong!"})


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class PostDetailView(APIView):
    serializer = PostSerializer

    def get(self, request, post_id):
        publication = get_object_or_404(Post, pk=post_id)
        serializer = self.serializer(publication)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        serializer = self.serializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, post_id):
        publication = get_object_or_404(Post, pk=post_id)
        publication.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UpvotePostView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.add_upvote()

        return Response(status=status.HTTP_200_OK)


class CommentsListView(APIView):
    serializer = CommentSerializer

    def get(self, request, post_id):
        comments = Comment.objects.filter(post__pk=post_id)
        serializer = self.serializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Comment.objects.create(post=post, **serializer.data)

        return Response(status=status.HTTP_201_CREATED)


class CommentDetailView(APIView):
    serializer = CommentSerializer

    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        serializer = self.serializer(comment)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        serializer = self.serializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
