# Generated by Django 3.1.4 on 2021-04-14 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mensajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('asunto', models.CharField(max_length=50)),
                ('texto', models.TextField()),
                ('leido', models.BooleanField(default=False)),
                ('id_Emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_Emisor', to=settings.AUTH_USER_MODEL)),
                ('id_Receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_Receptor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('foto', models.ImageField(upload_to='')),
                ('biografia', models.CharField(max_length=255)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('foto', models.ImageField(upload_to='')),
                ('idUsuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('informe', models.TextField()),
                ('realizada', models.BooleanField(default=False)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.cliente')),
                ('idEspecialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.especialista')),
            ],
        ),
    ]