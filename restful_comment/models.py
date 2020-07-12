from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django_comments.managers import CommentManager
from django_comments.models import Comment, CommentFlag, CommentAbstractModel

from vote.models import VoteModel


class RestfulCommentManager(CommentManager):
    def get_queryset(self):
        return super(RestfulCommentManager, self).get_queryset()

class RestfulCommentModel(VoteModel, Comment):
    object_id = models.UUIDField()
    father_id = models.UUIDField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()
    replies = ArrayField(models.UUIDField())

    def save():
        pass

    def get_comment_tree():
        pass
    
    
    

