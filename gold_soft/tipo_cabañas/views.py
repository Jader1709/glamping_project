from django.shortcuts import render, redirect

from tipo_cabañas.models import Tipo_cabaña

from .forms import Tipo_cabañaForm

def tipo_cabañas(request):    
    tipo_cabañas_list = Tipo_cabaña.objects.all()    
    return render(request, 'tipo_cabañas/index.html', {'tipo_cabañas_list': tipo_cabañas_list})

def change_status_tipo_cabaña(request, tipo_cabaña_id):
    tipo_cabaña = Tipo_cabaña.objects.get(pk=tipo_cabaña_id)
    tipo_cabaña.status = not tipo_cabaña.status
    tipo_cabaña.save()
    return redirect('tipo_cabañas')

def create_tipo_cabaña(request):
    form = Tipo_cabañaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tipo_cabañas')    
    return render(request, 'tipo_cabañas/create.html', {'form': form})