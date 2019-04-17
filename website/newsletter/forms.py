from django import forms


class NewsletterForm(forms.Form):

    email = forms.EmailField( label='',
        widget = forms.EmailInput(
            attrs={
                'placeholder' : 'email',
                'class':'px-4 border-2 border-secondary',
                'style':'border-radius:15px;'
            }
        )
    )
