from django.views.generic import TemplateView, FormView
from Auth.form import LoginForm
from django.contrib.auth import login, authenticate
from django.http.response import JsonResponse
from django.shortcuts import Http404,HttpResponseRedirect
from django.shortcuts import redirect


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if token:=request.GET.get('authtoken', None):
                pass

        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if user := authenticate(request, username=username, password=password):
                login(request, user)
                return redirect('main_page')
        raise Http404