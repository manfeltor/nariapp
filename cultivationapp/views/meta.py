# cultivationapp/views/meta.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from usersapp.decorators import management_required
from cultivationapp.models.meta import Sex, Species, Breed, PlantStatus, PlantPhase
from cultivationapp.forms.meta import SexForm, SpeciesForm, BreedForm, PlantStatusForm, PlantPhaseForm

@login_required
# @management_required
def meta_list_view(request, model_name):
    model_map = {
        'sex': (Sex, 'Sexo'),
        'species': (Species, 'Especie'),
        'breed': (Breed, 'Variedad'),
        'status': (PlantStatus, 'Estado'),
        'phase': (PlantPhase, 'Fase')
    }

    model_class, title = model_map.get(model_name, (None, None))
    if not model_class:
        return redirect('base')

    objects = model_class.objects.all()
    return render(request, 'meta/meta_list.html', {'objects': objects, 'model_name': model_name, 'title': title})

@login_required
# @management_required
def meta_create_view(request, model_name):
    form_class = _get_form_class(model_name)
    if not form_class:
        return redirect('base')

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('meta-list', model_name=model_name)
    else:
        form = form_class()

    return render(request, 'meta/meta_form.html', {'form': form, 'model_name': model_name, 'action': 'crear'})

@login_required
# @management_required
def meta_update_view(request, model_name, pk):
    form_class = _get_form_class(model_name)
    model_class = _get_model_class(model_name)

    if not form_class or not model_class:
        return redirect('base')

    instance = get_object_or_404(model_class, pk=pk)

    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('meta-list', model_name=model_name)
    else:
        form = form_class(instance=instance)

    return render(request, 'meta/meta_form.html', {'form': form, 'model_name': model_name, 'action': 'editar'})

@login_required
# @management_required
def meta_delete_view(request, model_name, pk):
    model_class = _get_model_class(model_name)
    if not model_class:
        return redirect('base')

    instance = get_object_or_404(model_class, pk=pk)

    if request.method == 'POST':
        instance.delete()
        return redirect('meta-list', model_name=model_name)

    return render(request, 'meta/meta_confirm_delete.html', {
        'object': instance,
        'model_name': model_name,
    })

def _get_form_class(model_name):
    return {
        'sex': SexForm,
        'species': SpeciesForm,
        'breed': BreedForm,
        'status': PlantStatusForm,
        'phase': PlantPhaseForm
    }.get(model_name)

def _get_model_class(model_name):
    return {
        'sex': Sex,
        'species': Species,
        'breed': Breed,
        'status': PlantStatus,
        'phase': PlantPhase
    }.get(model_name)
