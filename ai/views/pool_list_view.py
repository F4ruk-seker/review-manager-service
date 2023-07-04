from django.views.generic import ListView
from ai.models import CommentPool


class PoolView(ListView):
    queryset = CommentPool.objects.all()
    template_name = 'pool_list.html'


