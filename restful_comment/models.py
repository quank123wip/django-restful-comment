from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django_comments.managers import CommentManager
from django_comments.models import Comment, CommentFlag, CommentAbstractModel

from vote.models import VoteModel
from mptt.models import MPTTModel, TreeForeignKey


class RestfulCommentModel(VoteModel, Comment):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    replies = ArrayField(models.UUIDField())


    class MPTTMeta:
        order_insertion_by = ['submit_date']
    
    
    

