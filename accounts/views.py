from django.shortcuts import redirect, render
from .forms import RegistrationForm, ProfileForm, UserLoginForm
from .models import Profile

#send mail
from django.core.mail import send_mail

#authentication for login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

# def sign_up(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')

#     context = {
#         'form': form,
#     }        

#     return render(request, 'accounts/signup.html', context)


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        # password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Huff ,Username already exist')
            return redirect("signup")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Come On, Email was already Taken !')
            return redirect("signup")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            mydict = {'username': username}
            user.save()
            html_template = 'accounts/register_email.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Welcome to Service-Verse'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            return redirect('login')
    else:
        return render(request, 'accounts/signup.html')


def log_in(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Invalid Email or Password!!")
                
            context = {
                'form': form,
            }
            return render(request, 'accounts/login.html', context)
        

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('home')



def home(request):
    return render(request, 'accounts/profile.html')