from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import AccountForm, LoginForm
from .models import Account


class AccountView(View):
    def get(self, request):
        user = ''
        if request.user.is_authenticated:
            user = Account.objects.get(pk=request.user.id)
        return render(request, 'account/account.html', {'form': AccountForm, 'user': user})

    def post(self, request):
        form = AccountForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Account.objects.create_user(
                email=cd['email'],
                phone_number=cd['phone_number'],
                password=cd['password'],
                username=cd['username']
            )
            return redirect('account:account')


class AccountEditView(View):
    def get(self, request):
        form = AccountForm(instance=request.user)
        return render(request, 'account/profile_edit.html', {'form': form})

    def post(self, request):
        form = AccountForm(self.request.POST, instance=request.user)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            if cd['password'] != '':
                request.user.set_password(raw_password=cd['password'])
                request.user.save()
            return redirect('account:account')

        else:
            return render(request, 'account/profile_edit.html', {'form': form})


class LoginUserView(View):
    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('account:account')
            else:
                return redirect('account:account')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('account:account')
