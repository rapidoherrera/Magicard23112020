from django import forms

from .models import Post
from .models import Cliente

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('pseudonimo', 'nombre', 'clave', 'correo', 'telefono')