# Generated by Django 4.2.6 on 2023-10-13 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('estatura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('imc', models.IntegerField()),
                ('fecha_nac', models.DateField()),
                ('passwrd', models.CharField(max_length=12)),
            ],
        ),
    ]