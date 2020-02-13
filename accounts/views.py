from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        return redirect('api-index')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
