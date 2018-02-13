from django.db import models


class Post(models.Model):
    author = models.ForeignKey("auth.User")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
