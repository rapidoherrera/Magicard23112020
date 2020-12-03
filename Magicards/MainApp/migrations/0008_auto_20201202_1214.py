# Generated by Django 3.1.3 on 2020-12-02 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_auto_20201202_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='comuna',
        ),
        migrations.AddField(
            model_name='persona',
            name='correo',
            field=models.EmailField(default='deprueba@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='persona',
            name='direccion',
            field=models.CharField(default='direccion de prueba 123', max_length=100),
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='persona',
            name='telefono',
            field=models.CharField(default='12345678901', max_length=11),
        ),
    ]
