# Generated by Django 3.2.4 on 2021-06-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionCategoria', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('imagen', models.FileField(upload_to='uploads/')),
                ('descripcionProducto', models.CharField(max_length=150)),
                ('precio', models.FloatField()),
                ('categorias', models.ManyToManyField(to='TIENDAROPA.Categoria')),
            ],
        ),
    ]
