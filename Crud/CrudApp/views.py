from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Users
from .forms import UsersForms


def home(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGOUT_REDIRECT_URL, request.path))
    home = Users.objects.all()
    return render(request, 'home.html', {'users': home})


def new(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGOUT_REDIRECT_URL, request.path))
    form = UsersForms(request.POST or None, request.FILES or None)
    if form.is_valid():       
        form.save()
        return redirect('home')
    else:
        print(form.errors.as_data())
    return render(request, 'new.html', {'form': form})

def edit(request, id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGOUT_REDIRECT_URL, request.path))
    update = Users.objects.get(id=id)
    form = UsersForms(request.POST or None, request.FILES or None, instance=update)
    if form.is_valid():       
        form.save()
        return redirect('home')
    else:
        print(form.errors.as_data())
    return render(request, 'edit.html', {'form': form})
    
def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGOUT_REDIRECT_URL, request.path))
    dele = Users.objects.get(id=id)
    dele.delete()
    return redirect('home')
