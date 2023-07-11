from django.views.generic import TemplateView, FormView
from Auth.form import LoginForm
from django.contrib.auth import login, authenticate
from django.http.response import JsonResponse
from django.shortcuts import Http404,HttpResponseRedirect
from django.shortcuts import redirect

from Auth.models import AuthTokenModel

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if token := request.GET.get('authtoken', None):
                if token := AuthTokenModel.objects.filter(token=token).first():
                    if token.is_live():
                        login(request, token.user)
                        return redirect('home')

        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_page')