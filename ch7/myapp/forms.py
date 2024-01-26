from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data)<3:
            raise forms.ValidationError('hehehe')
        return data