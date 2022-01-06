from django.shortcuts import render,redirect
from django.contrib.auth import login, user_logged_out, authenticate
from django.contrib import messages



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request, "Something wrong, please try again...!")

    return render(request, 'login/log-reg.html')

def logoutpage(request):
    user = getattr(request, 'user', None)
    if hasattr(user, 'is_authenticated') and not user.is_authenticated():
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()

        return redirect('interface')

