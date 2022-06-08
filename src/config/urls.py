from django.contrib import admin
from django.urls import path, include, reverse, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('users/', include('users.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('news:list')))
]
