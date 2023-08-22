from django.shortcuts import render
from .models import Aplicação

# Create your views here.
def statuspage(request):
    aplicacoes = Aplicação.objects.all().order_by('nome')
    return render(request, 'statuspage.html',context={'aplicacoes':aplicacoes})