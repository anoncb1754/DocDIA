from django import forms


class TranscriptrForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea)