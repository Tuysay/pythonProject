
from django.contrib.auth.views import LoginView

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

from .forms import RegisterUserForm
from .models import Request, UserProfile
from django.views.generic.edit import CreateView
# Create your views here.


def index(request):
    return render(request, 'main/index.html')







def page_not_found(request, exception):
    return HttpResponseNotFound("Такой страницы не существует")


class BBLoginView(LoginView):
    template_name = 'registration/login.html'


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')



@login_required
def createprofile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'main/profile.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'main/profile.html')