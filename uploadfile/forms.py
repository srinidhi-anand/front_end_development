from django import forms
from uploadfile.models import Document
from django.forms.fields import FileField


class DocumentForm(forms.ModelForm):
    file = FileField(required=False)

    def clean_file(self):
        value = self.cleaned_data["file"]
        if str(value).split('.')[1].lower() != 'stp':
            raise forms.ValidationError('Not Supported')
        return 'False'

    class Meta:
        model = Document
        fields = ('description', )

