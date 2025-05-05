from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# def login(req):
#     return render(req, "login.html")

@login_required
def base(request):
    return render(request, 'base0.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True