from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    username = forms.CharField(max_length=50)

    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']
    
    def __init__(self, *args, **kargs) -> None:
        super(UserProfileForm, self).__init__(*args, **kargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'

    def save(self, commit=True):
        user_profile = super(UserProfileForm, self).save(commit=False)
        user_profile.user.username = self.cleaned_data['username']
        if commit:
            user_profile.user.save()    
            user_profile.save()

        return user_profile