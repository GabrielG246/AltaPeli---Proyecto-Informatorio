from django.shortcuts import render

def Inicio_View(request):
    return render(request, 'index.html')