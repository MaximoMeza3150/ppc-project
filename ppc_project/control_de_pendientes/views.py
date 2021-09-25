from django.shortcuts import render , redirect
from control_de_pendientes.models.Pending import Pending
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.


def feed(request):
    pendings = Pending.objects.all()
    context = { 'pendings' : pendings }
    return render( request , 'control_de_pendientes/feed.html' , context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'control_de_pendientes/register.html', context)


def registrar_pendiente(request):
    pass