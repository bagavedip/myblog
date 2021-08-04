from rest_framework import serializers
from .import models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        field = ['id', 'comment', 'blog_id', ]

