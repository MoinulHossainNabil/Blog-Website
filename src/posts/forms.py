from django import forms
from .models import Posts

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Type your comment',
        'id' : 'usercomment',
        'rows' : '4'
    }))
    class Meta:
        model = Posts
        fields = ('content',)