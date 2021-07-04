# Generated by Django 3.2.4 on 2021-07-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TIENDAROPA', '0002_carrito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categorias',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='TIENDAROPA.categoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(upload_to='static/'),
        ),
    ]
