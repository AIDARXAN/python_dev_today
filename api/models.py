from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractDateTimeModel(models.Model):
    creation_date = models.DateTimeField(_("Creation date"), auto_now_add=True)

    class Meta:
        abstract = True


class Post(AbstractDateTimeModel):
    title = models.CharField(_("Title"), max_length=256, unique=True)
    link = models.URLField(_("Link"), max_length=256, unique=True)
    up_votes = models.IntegerField(_("Up votes"), default=0)
    author_name = models.CharField(_("Author Name"), max_length=64)

    class Meta:
        db_table = "api_post"
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def add_upvote(self):
        self.up_votes += 1
        self.save()

    def update_post(self, data):
        self.title = data.get("title")
        self.link = data.get("link")
        self.author_name = data.get("author_name")
        self.save()


class Comment(AbstractDateTimeModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(_("Author Name"), max_length=64)
    content = models.TextField(_("Content"))

    class Meta:
        db_table = "api_comment"
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
