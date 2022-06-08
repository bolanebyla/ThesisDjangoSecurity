from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins

from . import models


def test(request):
    return render(request, 'news/news_list.html')


class NewsListView(generic.ListView):
    model = models.News
    template_name = 'news/news_list.html'


class NewsCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.News
    fields = ['title', 'text']
    success_url = reverse_lazy('news:list')
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
