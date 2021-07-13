from django.shortcuts import render
from django.views.generic.edit import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import LoginForm


# using FBV first but plan to move to CBV
def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(request, username=cd['username'], password=cd['password'])

      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponse('Authenticated successfully.')
        else:
          return HttpResponse('Disabled account.')
      else:
        return HttpResponse('Invalid login.')
    else:
      form = LoginForm()
    
    context = {
      'form': form
    }
    return render(request, 'account/login.html', context)

# # Create your views here.
# class LoginView(View):
#   pass

# class LogoutView(View):
#   pass

# class RegisterView(View):
#   pass