from django.db import models


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    comment = models.TextField(max_length=255)
    blog_id = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

