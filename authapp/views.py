from django.shortcuts import render, redirect
from django.views import View

from authapp.forms import UserForm


class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        return render(
            request,
            'authapp/user_form.html',
            context={
                'form': form,
            }
        )

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect("authapp:user-create")
