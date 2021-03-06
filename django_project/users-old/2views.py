    def register(request):
    	if request.method == "POST":
    		form = UserRegisterForm(request.POST)
    		# form = UserCreationForm(request.POST)
                    print(f"POST: {request.POST}")
    ​
    		if form.is_valid():
                            print("form is valid")
    			form.save()
    			username = form.cleaned_data.get('username')
    			messages.success(request, f'Account created for {username}!')
    			return redirect('blog-home')
                    else:
                            print("form is NOT valid")
    	else:
                    print(f"Request method is {request.method}")
    		form = UserRegisterForm()
    		# form = UserCreationForm()
    ​
    	form_errs = form.errors.as_data()
    	form_errs_repr = repr(form_errs)
    ​
    	context = {
    		'form': form, 
    		'form_errs': form_errs,
    		'form_errs_repr': form_errs_repr,
    	}
    ​
    	return render(request, 'users/register.html', context)
