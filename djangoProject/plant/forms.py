from django import forms

from djangoProject.plant.models import ProfileModel, PlantModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('username', 'first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Second Name',
            'profile_picture': 'Profile Picture',
        }


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            PlantModel.objects \
                .all() \
                .delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'
        labels = {
            'plant_type': 'Type',
            'name': 'Name',
            'image_url': 'Image Url',
            'description': 'Description',
            'price': 'Price',
        }


class PlantEditForm(PlantBaseForm):
    pass


class PlantCreateForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
