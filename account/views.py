from django.shortcuts import render
from django.views.generic.edit import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import LoginForm


# using FBV first but plan to move to CBV


# # Create your views here.
class LoginView(View):
  template_name = 'account/login.html'

  def post(self, request):
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
  
  def get(self, request):
    form = LoginForm()
    
    context = {
      'form': form
    }
    return render(request, self.template_name, context)

# class LogoutView(View):
#   pass

# class RegisterView(View):
#   pass