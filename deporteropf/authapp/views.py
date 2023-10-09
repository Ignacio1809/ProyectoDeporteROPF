from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        number=request.POST.get('usernumber')
        firstname=request.POST.get('fname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            message.info(request, "Las contraseñas ingresadas no son iguales.")
            return redirect('/signup')


def handlelogin(request):
    return render(request,"handlelogin.html")
