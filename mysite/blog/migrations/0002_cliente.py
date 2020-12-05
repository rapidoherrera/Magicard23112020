# Generated by Django 3.1.2 on 2020-10-31 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('clave', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=11)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
