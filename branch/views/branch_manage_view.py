from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from branch.models import BranchModel


class BranchListView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "branch_list_manage_view.html")


class BranchManager(DetailView):

    queryset = BranchModel.objects.all()
    pk_url_kwarg = 'branch_id'
    context_object_name = 'branch'
    template_name = 'branch_manager.html'

    # def get_context_data(self, **kwargs):
    #     context: dict = super(self).get_context_data(**kwargs)
    #     return context
    #
