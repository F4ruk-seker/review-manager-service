from django.shortcuts import render
from django.views.generic import View, ListView


class BranchManager(View):

    def get(self, request, *args, **kwargs):
        return render(request, "branch_manager.html")
