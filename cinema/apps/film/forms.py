from django import forms

from ..comments.models import FilmComments


# class FilmCommentsForm(forms.ModelForm):
#     # author = forms.CharField(widget=forms.TextInput(
#     #     attrs={'placeholder': 'Author',
#     #            'class': 'form-control'}))
#     text = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder': 'Text',
#                'class': 'form-control'}))
#
#     class Meta:
#         model = FilmComments
#         fields = ('text',)

class FilmCommentsForm(forms.ModelForm):
    class Meta:
        model = FilmComments
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Введите текст комментария',
                                                  'class': 'form-control'}),
        }