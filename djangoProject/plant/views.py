from django.shortcuts import render, redirect

from djangoProject.plant.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from djangoProject.plant.models import ProfileModel, PlantModel


def get_user_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def index(request):
    profile = get_user_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'core/home-page.html', context)


def catalogue(request):
    plants = PlantModel.objects.all()

    context = {
        'plants': plants,
    }

    return render(request, 'core/catalogue.html', context)


def add_plant(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'plant/create-plant.html', context)


def details_plant(request, pk):
    plant = PlantModel.objects.filter(pk=pk).get()

    context = {
        'plant': plant,
    }

    return render(request, 'plant/plant-details.html', context)


def edit_plant(request, pk):
    plant = PlantModel.objects. \
        filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'plant/edit-plant.html', context)


def delete_plant(request, pk):
    plant = PlantModel.objects. \
        filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'plant/delete-plant.html', context)


def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_user_profile()
    plants_count = PlantModel.objects.count()

    context = {
        'profile': profile,
        'plants_count': plants_count,
    }

    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = get_user_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_user_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)


