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

    # this is for displaying from the template
    if use_form_subclass:
        form_string = 'UserRegisterForm'
    else:
        form_string = 'UserCreationForm'

    # if call_isvalid is true, the view will call and provide
    # the function return value, of form.is_valid(), whereas
    # if call_isvalid is false, the view will NEVER call
    # form.is_valid(). Change this to True or False to
    # choose whether to call it or not.
    call_isvalid = True

    # validform will recieve the answer to form.is_valid(),
    # only for the purpose of showing that answer. There
    # is NO need to change this.
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
