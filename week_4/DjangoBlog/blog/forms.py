from django.forms import ModelForm

from blog.models import Comment, Post


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment_body']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status']