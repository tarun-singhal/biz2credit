from django import forms

class StoryForm(forms.Form):
    title = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    content = forms.CharField(
        max_length=20000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    status = forms.ChoiceField(choices=(('0', 'Draft'),('1', 'Published')))

    def clean(self):
        cleaned_data = super(StoryForm, self).clean()
        title = cleaned_data.get('title')
        email = cleaned_data.get('email')
        content = cleaned_data.get('content')
        status = cleaned_data.get('status')

        if not title and not email:
            raise forms.ValidationError('You have to write something!')