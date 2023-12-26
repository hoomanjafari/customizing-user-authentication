from django.shortcuts import render, redirect
from django.views import View
from .forms import AccountForm
from .models import Account


class AccountView(View):
    def get(self, request):
        return render(request, 'account/account.html', {'form': AccountForm})

    def post(self, request):
        form = AccountForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Account.objects.create_user(
                email=cd['email'],
                phone_number=cd['phone_number'],
                password=cd['password'],
            )
            return redirect('account:account')
