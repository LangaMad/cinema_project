from django import forms

from ..comments.models import PostComment

class PostCommentsForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Введите текст отзыва',
                                                  'class': 'form-control'}),
        }

class SearchFormNews(forms.Form):
    query = forms.CharField(max_length=200, required=False)
