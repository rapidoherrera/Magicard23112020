from django.test import TestCase
from apps.Registro.models import Cuenta
from apps.Registro.forms import CuentaForm

class CuentaFormCase(TestCase):
        
    def test_valid_form(self):
        cuenta = Cuenta.objects.create(alias='depper',edad=19, descripcion='negro')
        data = {'alias': cuenta.alias, 'edad': cuenta.edad, 
        'descripcion': cuenta.descripcion }
        form = CuentaForm(data=data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        cuenta = Cuenta.objects.create(alias='',edad=19, descripcion="asasa")
        data = {'alias': cuenta.alias, 'edad': cuenta.edad,'descripcion': cuenta.descripcion, }
        form = CuentaForm(data=data)
        self.assertFalse(form.is_valid())
