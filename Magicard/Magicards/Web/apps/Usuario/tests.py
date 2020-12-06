from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTest(TestCase):

    def test_user_creation(self):
        users = User.objects.all()
        cant_previa = users.count()
        User(email = "prueba@prueba.com", username='prueba user').save()
        cant_post = users.count()
        #si las cantidades coinciden es que si agrego el usuario de prueba
        self.assertEquals(cant_post, cant_previa + 1)
        
    def test_user_delete(self):
        users = User.objects.all()
        cant_previa = users.count()
        User(email = "prueba@prueba.com", username='prueba user').delete()
        cant_post = users.count()
        #si las cantidades coinciden es que si elimino el usuario de prueba
        self.assertEquals(cant_post + 1, cant_previa)    