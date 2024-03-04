from django import forms
from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                self.add_error("password", forms.ValidationError("Password invalid"))
            else:
                return self.cleaned_data
        except User.DoesNotExist:
            self.add_error("username", forms.ValidationError("User does not exists"))


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username",)

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        user.save()