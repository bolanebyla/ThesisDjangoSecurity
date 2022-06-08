from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/auth/signup.html'

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        messages.success(self.request, 'Вы успешно зарегестрировалась! Используйте свои данные для входа')
        return response
