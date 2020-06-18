from django.views import View
from django.shortcuts import render
from common.forms import LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    def get(self, request):
        return render(request, 'loginpage.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

            if user:
                login(request, user)
                return HttpResponseRedirect('/admin/')
            return render(request, 'loginpage.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
