from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)

		print(f"request.POST: {request.POST}") # test

		if form.is_valid():
			print("form is valid") # test
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('blog-home')
	else:
		form = UserRegisterForm()

	form_errs = form.errors.as_data()
	form_errs_repr = repr(form_errs)

	context = {
		'form': form, 
		'form_errs': form_errs,
		'form_errs_repr': form_errs_repr,
	}

	return render(request, 'users/register.html', context)
