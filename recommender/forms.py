from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=50, initial="your name")

class EmailForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))