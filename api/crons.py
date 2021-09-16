from api.models import Post


def resetting_up_votes():
    posts = Post.objects.filter(up_votes__gt=0)
    for post in posts:
        post.up_votes = 0
        post.save()
