from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Imovei, Cidade
from django.shortcuts import get_object_or_404

# Página só pode ser acessada quando logado, se não, redireciona
@login_required(login_url='/auth/logar/')
def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    # Pegar todos os tipos
    tipo = request.GET.getlist('tipo')
    cidades = Cidade.objects.all()
    # Se o usuário filtrou algo
    if preco_minimo or preco_maximo or cidade or tipo:
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999
        if not tipo:
            tipo = ['A', 'C']
        imoveis = Imovei.objects.filter(valor__gte=preco_minimo)\
        .filter(valor__lte=preco_maximo)\
        .filter(tipo_imovel__in=tipo).filter(cidade=cidade)
    else:
        imoveis = Imovei.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})

# Além de request, recebo id do urls.py
def imovel(request, id):
    # Busque o imóvel no banco de dados, se não encontrar, mandar erro 404
    imovel = get_object_or_404(Imovei, id=id)
    # Exclui imóvel já visualizado e exibe 2 
    sugestoes = Imovei.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    return render(request, 'imovel.html', {'imovel': imovel})