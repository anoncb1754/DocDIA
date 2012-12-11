from django import forms


class TranscriptrForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea)

class ProjectForm(forms.Form):
        CHOICES = (
                ('0', 'Public'),
                ('1', 'Private'),
                )
        project_name = forms.CharField()
        project_description = forms.CharField(widget=forms.Textarea)
        doc_1 = forms.FileField(label="Select a document page(1): ",
                help_text="max. 4MB")
        #doc_2 = forms.FileField(label="Select a document page(2): ",
                # help_text="max. 4MB")
        status = forms.ChoiceField(choices=CHOICES)
