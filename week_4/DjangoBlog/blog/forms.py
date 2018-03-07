from django import forms

from blog.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment_body']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status']

class ContactForm(forms.Form):
    email_id = forms.EmailField()
    subject = forms.CharField(max_length=50)
    body = forms.CharField(max_length=200, widget=forms.Textarea)