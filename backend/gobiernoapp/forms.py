from django import forms

class CommentForm(forms.Form):
    comm_content = forms.CharField()
