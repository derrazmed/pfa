from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomRegistrationForm
from accounts.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render



class SignUpView(CreateView):
    form_class = form_class = CustomRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        username=form.cleaned_data['username']
        email=form.cleaned_data['email']
        password=form.cleaned_data['password']
        if form.is_valid():
            user = User.objects.create_user(username,email,password)
            user.save()
            return redirect('login')
        else:
            return render(request, '/')
    else:
        form = CustomRegistrationForm()
        return render(request, '/')

