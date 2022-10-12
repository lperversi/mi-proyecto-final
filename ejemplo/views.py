from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html",{'nombre':'Leandro',
                                                'apellido':'Perversi'})

def index_dos(request):
    return render(request, "ejemplo/saludar.html",{'nombre':nombre,
                                                'apellido':apellido})

def index_tres(request):
    return render(request, "ejemplo/saludar.html",{'notas':[1,2,3,4,5,6,7]})

def imc(request,peso,altura):
    imc = (peso/(altura*altura))
    return render(request,"ejemplo/imc.html",{'imc': imc})