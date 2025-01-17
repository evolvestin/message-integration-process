from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Message, Mail
from .services.mail_service import MailBox


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # перенаправление на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    # request.POST['is_credentials_wrong'] = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('messages')  # перенаправление после успешного входа
        else:
            is_credentials_wrong = True
            return render(request, 'login.html', {'is_credentials_wrong': is_credentials_wrong})
    return render(request, 'login.html')


def mail(request, is_credentials_valid='True'):
    context = {
        'is_credentials_valid': is_credentials_valid
    }
    return render(request, 'mail.html', context)


@login_required
def messages(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    context = {
        'email': email
    }

    if email and password and MailBox.is_credentials_valid(email, password):

        if not Mail.objects.filter(mail=email, password=password).exists():
            mail_data = {
                'mail': email,
                'password': password,
                'mail_type': MailBox.get_imap_server_by_email(email),
                'last_message_id': 0,
            }
            MailBox.add_new_mail(mail_data)

        if Mail.objects.filter(mail=email, password=password).exists():
            stored_messages = Message.objects.all()
            context['stored_messages'] = stored_messages
        # last_message = Message.objects.filter(mail=email).latest()
        mail_obj = Mail.objects.get(mail=email)
        password = mail_obj.password
        context['password'] = password
        # context['last_message'] = last_message
        return render(request, 'messages.html', context)
    else:
        return render(request, 'mail.html',
                      {'is_credentials_valid': 'False'})  # перенаправление после успешного входаx
