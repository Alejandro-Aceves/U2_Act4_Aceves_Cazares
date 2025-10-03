from django.shortcuts import render

# Create your views here.
def index(request):
        instrumentos = [
            {'nombre': 'Guitarra Eléctrica', 'precio': 599.99, 'marca': 'Fender'},
            {'nombre': 'Batería Acústica', 'precio': 1200.00, 'marca': 'Pearl'},
            {'nombre': 'Teclado Sintetizador', 'precio': 850.50, 'marca': 'Roland'},
        ]
        contexto = {'instrumentos': instrumentos}
        return render(request, 'index.html', contexto)