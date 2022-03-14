# django_project/users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

def register(request):
    if request.method != 'POST': # form method is anything but post
        form = UserCreationForm()
    else: # form method is post
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    return render(request, 'users/register.html', {'form': form} )

def testreg(request):

    # if use_form_subclass is True, the view will create and
    # render the subclass of UserCreationForm, which is
    # UserRegisterForm.
    #
    # if use_form_subclass is False, the view will create and
    # use the -non-subclass, UserCreationForm
    #
    # choose which you'd like by setting it to True or False,
    # below:
    use_form_subclass = True
    call_isvalid = True
    validform = False

    if request.method != 'POST': # form method is anything but post
        form = UserRegisterForm()
    else: # form method is post
        form = UserRegisterForm(request.POST)

        if call_isvalid:
            validform = form.is_valid()

    yesno = {False: 'no', True: 'yes'}

    context = {
        'form': form,
        'validform': yesno[validform],
        'call_isvalid': yesno[call_isvalid]
    }

    return render(request, 'users/testreg.html', context )

@login_required
def profile(request):
    return render(request, 'users/profile.html')
