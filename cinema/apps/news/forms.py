from django import forms

from ..comments.models import PostComment

class PostCommentsForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Введите текст комментария',
                                                  'class': 'form-control'}),
        }