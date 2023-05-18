from django.contrib import admin

from djangoProject.plant.models import PlantModel, ProfileModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(PlantModel)
class AlbumAdmin(admin.ModelAdmin):
    pass
