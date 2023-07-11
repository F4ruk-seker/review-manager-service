from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'index.html'

    @classmethod
    def as_view(cls, **initkwargs):
        return login_required(super().as_view(**initkwargs))

