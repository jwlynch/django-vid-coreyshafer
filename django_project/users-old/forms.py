from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']