from django.urls import path
from api import views


urlpatterns = [
    path("ping/", views.ping, name="ping"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("post/<int:post_id>/", views.PostDetailView.as_view(), name="post_detail"),
    path(
        "post/<int:post_id>/upvote/", views.UpvotePostView.as_view(), name="upvote_post"
    ),
    path(
        "post/<int:post_id>/comments/",
        views.CommentsListView.as_view(),
        name="comments_list",
    ),
    path(
        "comment/<int:comment_id>/",
        views.CommentDetailView.as_view(),
        name="comment_detail",
    ),
]
