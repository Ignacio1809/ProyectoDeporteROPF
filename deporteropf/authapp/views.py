from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import re
from .models import cliente
# Create your views here.
def Home(request):
    return render(request,"index.html")

def is_valid_gmail(email):
    """Verifica si el correo electrónico proporcionado tiene un formato de Gmail válido."""
    pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    return re.match(pattern, email)

#def signup(request):
    if request.method=="POST":
        number=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        username = email.split('@')[0]

        if len(number)>9 or len(number)<9:
            messages.info(request, "El telefono ingresado debe tener al menos 9 dígitos")
            return redirect('/signup')
        
        if pass1!=pass2:
            messages.info(request, "Las contraseñas ingresadas no son iguales.")
            return redirect('/signup')
        
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Este nombre de usuario ya ha sido registrado.")
            return redirect('/signup')
        
        if not is_valid_gmail(email):
            messages.warning(request, "Por favor, ingrese una dirección de Gmail válida.")
            return redirect('/signup')
        
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Este correo ya ha sido registrado")
            return redirect ('/signup')

        user=User.objects.create_user(username=username, email=email, password=pass1)
        user.save()
        messages.success(request, "El usuario ha sido creado, por favor inicie sesión.")
        return redirect('/login')

    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')

        user = authenticate(request, username=email, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión exitosamente.")
            return redirect('/')
        else:
            messages.error(request, "Credenciales Invalidas")
            return redirect('/login')


    return render(request,"handlelogin.html")

def signup(request):
    if request.method == 'POST':
        number = request.POST['usernumber']
        name = request.POST['fname']
        lname = request.POST['lastname']
        email = request.POST['email']
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])/100
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        imc = weight/height**2
        birth= request.POST['birthdate']

        if len(number)>9 or len(number)<9:
            messages.info(request, "El telefono ingresado debe tener al menos 9 dígitos")
            return redirect('/signup')
       
        if pass1!=pass2:
            messages.info(request, "Las contraseñas ingresadas no son iguales.")
            return redirect('/signup')
        else:
            passwrd= pass1
        if cliente.objects.filter(email=email).exists():
            messages.info(request, "El correo electrónico ingresado ya está en uso.")
            return redirect('/signup')

        usuario = cliente.objects.create(
            telefono=number, nombre=name, apellido=lname,email=email, estatura=height, peso=weight, imc=imc, fecha_nac=birth, passwrd=passwrd)

        # Authenticate the user
        messages.info(request, "Usuario creado con éxito.")
        return redirect('/login')
    return render(request,"signup.html")
    

def handleLogout(request):
    logout(request)
    messages.success(request, "Has cerrado tu sesión exitosamente")
    return redirect('/login')