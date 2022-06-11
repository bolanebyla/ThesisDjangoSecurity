from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins

from . import models


class NewsListView(generic.ListView):
    model = models.News
    template_name = 'news/news_list.html'
    paginate_by = 5


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


class NewsUpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.News
    fields = ['title', 'text']
    success_url = reverse_lazy('news:list')
    template_name = 'news/news_form.html'

    def get_object(self, queryset=None):
        obj: models.News = super(NewsUpdateView, self).get_object(queryset)

        if self.request.user.is_staff or obj.author == self.request.user:
            return obj
        raise Http404
