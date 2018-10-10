from django import forms
from django.contrib.auth.models import User
from vid_corner_app.models import UserProfileInfo



class UserForm(forms.ModelForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder':'Username'}
        )
    )

    email = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder':'Email'}
            )
        )
    
    password=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password'}
            )
        )

    confirm_password=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder':'Confirm Password'}
            )
        )
    class Meta:
        model=User
        fields=('username','email','password')
        help_texts = {
            'username': None,
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match, please try again!")




class UserProfileInfoForm(forms.ModelForm):

    about=forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'placeholder':'Give some details about your channel! What kind of content will you be uploading?'}
            )
        )
    
    class Meta():
        model = UserProfileInfo
        fields = ('channel_name', 'about', 'profile_picture', 'header_picture',)
