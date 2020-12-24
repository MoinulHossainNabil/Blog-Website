from django import forms
from .models import Posts
from tinymce.widgets import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Posts
        fields = (
            'post_author', 'title', 'body', 'content', 'category', 'thmbnail', 'featured', 'previous_post', 'next_post')

# class CommentForm(forms.ModelForm):
#     # content = forms.CharField(widget=forms.Textarea(attrs={
#     #     'class' : 'form-control',
#     #     'placeholder' : 'Type your comment',
#     #     'id' : 'usercomment',
#     #     'rows' : '4'
#     # }))
#     class Meta:
#         model = Posts
#         fields = ('content',)
