from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return redirect('login')
def home(requests):
    return render(requests,'personalapp/home.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})