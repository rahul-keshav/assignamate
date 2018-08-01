from django import forms
from home.models import Post,Assignment_discussion,Assignment_discussion_reply

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control' ,
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)

class Assignment_discussion_form(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your comment...'
        }
    ))
    class Meta:
        model = Assignment_discussion
        fields=('comment',)

class Assignment_discussion_reply_form(forms.ModelForm):
    reply = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your comment...'
        }
    ))
    class Meta:
        model = Assignment_discussion_reply
        fields=('reply',)

