from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def usersList(request):
    users = CustomUser.objects.all()  # Retrieve all users
    return render(request, 'userslist.html', {'users': users})

@login_required
def create_eliminate_user_view(request):
    # if not request.user.is_superuser:
    #     return redirect('unauthorized')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userslist')
    else:
        form = CustomUserCreationForm()

    return render(request, 'create_user.html', {'form': form})

class CreateEliminateUserView(LoginRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('userslist')

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('userslist')

    def test_func(self):
        return self.request.user.is_staff and self.request.user != self.get_object() and self.get_object().username != 'admin'
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        username = self.object.username
        response = super().delete(request, *args, **kwargs)
        messages.warning(request, f"Usuario '{username}' correctamente eliminado.")
        return response