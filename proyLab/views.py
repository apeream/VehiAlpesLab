from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import ProspectoForm, Perfil, PerfilVendedor, Vendedor


def index(request):
    context = {'form': ProspectoForm()}
    return render(request, 'proyLab/index.html', context)

def agregar_prospecto(request):
    if request.method == 'POST':
        vendedores = []
        perfil = None
        form = ProspectoForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            rango = cleaned_data.get('rango')
            tieneCarro = cleaned_data.get('tieneCarro')
            perfil = Perfil.objects.get(rango=rango, tieneCarro=tieneCarro)
            if perfil is not None:
                vendedores = Vendedor.objects.filter(perfil=perfil)
            form.save()
            #return HttpResponseRedirect(reverse('proy:index'))
    else:
        vendedores = []
        perfil = None
        form = ProspectoForm()
    return render(request, 'proyLab/index.html', {'form': form, 'vendedores': vendedores, 'perfil': perfil})

