from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from quiz.models import Category
from .forms import SignUpForm

# Create your views here.
@login_required
def index(request):
    category = Category.objects.order_by('name')
    # thread = Thread.objects.all()
    my_dic ={'category':category}
    return render(request,'registration/home.html',context=my_dic)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
