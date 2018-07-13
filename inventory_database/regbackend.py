from registration.backends.default.views import RegistrationView
from inventory_database.forms import EditorForm
from .models import Editor


class MyRegistrationView(RegistrationView):

    form_class = EditorForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        p = form_class.cleaned_data['Editor']
        new_profile = Profile.objects.create(user=new_user, is_editor=p)
        new_profile.save()
        return new_user