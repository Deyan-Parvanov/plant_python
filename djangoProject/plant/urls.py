from django.urls import path, include

from djangoProject.plant.views import index, details_plant, add_plant, edit_plant, delete_plant, catalogue, add_profile, \
    details_profile, edit_profile, delete_profile

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('plant/', include([
        path('details/<int:pk>/', details_plant, name='details plant'),
        path('add/', add_plant, name='add plant'),
        path('edit/<int:pk>/', edit_plant, name='edit plant'),
        path('delete/<int:pk>/', delete_plant, name='delete plant'),
    ])),
    path('profile/', include([
        path('add/', add_profile, name='add profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
