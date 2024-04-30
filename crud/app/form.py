from django.forms import ModelForm
from app.models import Usuario

# Create the form class.
class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ["id_user", "nome", "idade", "tipo"]